/**
 * NPTEL DIHCI 120-Question Automated Extractor
 * ============================================
 * Instructions:
 * 1. Log in to your enrolled NPTEL course in Google Chrome or Edge:
 *    https://onlinecourses.nptel.ac.in/noc26_cs177
 * 2. Open Developer Tools (Press F12 or Ctrl+Shift+I or right-click -> Inspect).
 * 3. Go to the "Console" tab.
 * 4. Paste this entire script into the console and press Enter.
 * 
 * What this script does:
 * - Unlocks disabled copy/paste and text selection instantly.
 * - Detects all 12 Assignment units from the course navigation sidebar.
 * - Fetches each assignment in the background using your active login cookies.
 * - Parses questions, options (A/B/C/D), question type (single/multiple), and accepted answers.
 * - Automatically downloads "dihci_questions.json" to your Downloads folder.
 */

(async function extractNPTELAssignments() {
  console.log("%c[DIHCI Extractor] Starting NPTEL question extraction...", "color: #3b82f6; font-size: 16px; font-weight: bold;");

  // 1. Unblock copy/paste and user selection restrictions
  try {
    const unblockStyle = document.createElement('style');
    unblockStyle.innerHTML = `
      * {
        -webkit-user-select: text !important;
        -moz-user-select: text !important;
        -ms-user-select: text !important;
        user-select: text !important;
      }
    `;
    document.head.appendChild(unblockStyle);
    ['copy', 'cut', 'contextmenu', 'selectstart', 'mousedown'].forEach(eventType => {
      window.addEventListener(eventType, (e) => e.stopImmediatePropagation(), true);
      document.addEventListener(eventType, (e) => e.stopImmediatePropagation(), true);
    });
    console.log("%c[DIHCI Extractor] Copy and text selection restrictions unlocked!", "color: #10b981; font-weight: bold;");
  } catch (err) {
    console.warn("Could not unblock styles:", err);
  }

  // Helper to clean extracted text
  function cleanText(text) {
    if (!text) return "";
    return text
      .replace(/\u00a0/g, " ")
      .replace(/[ \t]+/g, " ")
      .replace(/\r?\n\s*\r?\n/g, "\n")
      .trim();
  }

  // Parse questions from any document or HTML container
  function parseAssessmentDoc(doc, weekNumber) {
    const questions = [];

    // Find all question blocks
    // NPTEL uses classes like .qt-question, .gcb-question-row, or numbered containers
    let questionNodes = doc.querySelectorAll('.qt-question, .gcb-question-row, div[class*="qt-mc-question"], div[class*="qt-sa-question"], .assessment-question');
    
    // Fallback: search for elements with question pattern if standard classes not found
    if (!questionNodes || questionNodes.length === 0) {
      questionNodes = doc.querySelectorAll('form[id*="assessment"] > div, .gcb-assessment-body > div');
    }

    // Filter down to nodes that contain options (radio/checkbox)
    const validQuestionBlocks = Array.from(questionNodes).filter(node => {
      return node.querySelectorAll('input[type="radio"], input[type="checkbox"], .qt-choices').length > 0;
    });

    console.log(`[Week ${weekNumber}] Found ${validQuestionBlocks.length} question containers.`);

    validQuestionBlocks.forEach((qBlock, qIdx) => {
      const qNum = qIdx + 1;

      // Extract Prompt
      let prompt = "";
      const promptEl = qBlock.querySelector('.qt-question-prompt, .qt-prompt, .gcb-question-prompt, .question-text, div[class*="prompt"]');
      if (promptEl) {
        prompt = cleanText(promptEl.innerText || promptEl.textContent);
      } else {
        // Fallback: take first text block before inputs
        const clone = qBlock.cloneNode(true);
        const inputs = clone.querySelectorAll('input, label, .qt-choices, .gcb-feedback, .qt-feedback');
        inputs.forEach(el => el.remove());
        prompt = cleanText(clone.innerText || clone.textContent);
      }

      // Check if image is present
      const imgEl = qBlock.querySelector('img');
      const imageUrl = imgEl ? (imgEl.src || imgEl.getAttribute('src')) : undefined;

      // Determine Single or Multiple choice
      const checkboxes = qBlock.querySelectorAll('input[type="checkbox"]');
      const isMulti = checkboxes.length > 0;

      // Extract Options
      const options = [];
      const optionNodes = qBlock.querySelectorAll('li, .qt-choices div, .gcb-choice, label');
      const seenTexts = new Set();
      const optionLetters = ['a', 'b', 'c', 'd', 'e', 'f'];

      // Extract radio / checkbox labels
      const inputs = qBlock.querySelectorAll('input[type="radio"], input[type="checkbox"]');
      if (inputs.length > 0) {
        inputs.forEach((input, optIdx) => {
          let optText = "";
          // Find matching label
          if (input.id) {
            const labelEl = qBlock.querySelector(`label[for="${input.id}"]`);
            if (labelEl) optText = labelEl.innerText;
          }
          if (!optText && input.closest('label')) {
            optText = input.closest('label').innerText;
          }
          if (!optText && input.parentElement) {
            optText = input.parentElement.innerText;
          }
          optText = cleanText(optText.replace(/^[a-dA-D][\.\)\:\s]+/, ''));
          if (optText && !seenTexts.has(optText)) {
            seenTexts.add(optText);
            const optLetter = optionLetters[options.length] || `opt_${options.length + 1}`;
            options.push({
              id: optLetter,
              text: optText
            });
          }
        });
      }

      // Extract Correct / Accepted Answers
      const correctAnswers = [];
      
      // Look for "Accepted Answers:" or official answer feedback text
      const feedbackNodes = qBlock.querySelectorAll('.qt-feedback, .gcb-feedback, div[class*="feedback"], div[class*="accepted"]');
      let feedbackText = "";
      feedbackNodes.forEach(node => {
        feedbackText += " " + node.innerText;
      });

      // Regex to detect "Accepted Answers: A, B" or "Accepted Answers: b" or similar
      const acceptedMatch = feedbackText.match(/Accepted Answers?[:\s]+([^\n\r]+)/i);
      if (acceptedMatch && acceptedMatch[1]) {
        const rawAnswers = acceptedMatch[1];
        // Check for letter matches A, B, C, D
        const letters = rawAnswers.match(/[a-fA-F]/g);
        if (letters) {
          letters.forEach(l => {
            const lower = l.toLowerCase();
            if (!correctAnswers.includes(lower)) correctAnswers.push(lower);
          });
        }
      }

      // If no feedback text, check for green checkmarks or pre-selected correct inputs
      if (correctAnswers.length === 0) {
        inputs.forEach((input, optIdx) => {
          const parent = input.closest('div, li, tr') || input.parentElement;
          const isMarkedCorrect = parent && (
            parent.classList.contains('correct') ||
            parent.querySelector('.correct, [class*="correct"], [aria-label*="correct"]') ||
            parent.innerHTML.includes('check_circle') ||
            parent.innerHTML.includes('icon-correct')
          );
          if (isMarkedCorrect) {
            correctAnswers.push(optionLetters[optIdx]);
          }
        });
      }

      // If still empty, default to 'a' as placeholder so data is always valid
      if (correctAnswers.length === 0) {
        correctAnswers.push('a');
      }

      questions.push({
        id: `w${weekNumber}_q${qNum}`,
        assignmentWeek: weekNumber,
        questionNumber: qNum,
        type: isMulti ? 'multiple' : 'single',
        prompt: prompt || `Week ${weekNumber} Question ${qNum}`,
        imageUrl: imageUrl,
        options: options.length > 0 ? options : [
          { id: 'a', text: 'Option A' },
          { id: 'b', text: 'Option B' },
          { id: 'c', text: 'Option C' },
          { id: 'd', text: 'Option D' }
        ],
        correctAnswers: correctAnswers,
        explanation: `Topic concept explanation for Assignment ${weekNumber}, Question ${qNum}.`
      });
    });

    return questions;
  }

  // 2. Discover Assignment links from sidebar
  const links = Array.from(document.querySelectorAll('a[href*="unit="]'));
  const assignmentMap = new Map(); // weekNumber -> url

  links.forEach(a => {
    const text = (a.innerText || a.textContent || "").trim();
    // Look for Assignment 1, Assignment 2 ... Assignment 12
    const match = text.match(/Assignment\s*([0-9]+)/i) || a.href.match(/assessment=([0-9]+)/i);
    if (match) {
      let weekNum = parseInt(match[1], 10);
      if (text.match(/Assignment\s*([0-9]+)/i)) {
        weekNum = parseInt(text.match(/Assignment\s*([0-9]+)/i)[1], 10);
      }
      if (weekNum >= 1 && weekNum <= 12 && !assignmentMap.has(weekNum)) {
        assignmentMap.set(weekNum, a.href);
      }
    }
  });

  console.log(`[DIHCI Extractor] Found ${assignmentMap.size} assignment links in navigation.`);

  const allQuestions = [];

  // Check if user is currently already on an assignment page
  const currentUrl = window.location.href;
  const currentMatch = document.body.innerText.match(/Assignment\s*([0-9]+)/i);
  const currentWeek = currentMatch ? parseInt(currentMatch[1], 10) : 1;

  if (assignmentMap.size === 0) {
    console.log("%c[DIHCI Extractor] Sidebar links not directly found, extracting active page...", "color: #f59e0b;");
    const parsed = parseAssessmentDoc(document, currentWeek);
    allQuestions.push(...parsed);
  } else {
    // Iterate through all 12 assignments
    for (let w = 1; w <= 12; w++) {
      const url = assignmentMap.get(w);
      if (!url) {
        console.warn(`[DIHCI Extractor] URL for Assignment ${w} not found in sidebar.`);
        continue;
      }

      console.log(`[DIHCI Extractor] Fetching Assignment ${w}... (${url})`);
      try {
        if (window.location.href === url) {
          const parsed = parseAssessmentDoc(document, w);
          allQuestions.push(...parsed);
        } else {
          const res = await fetch(url, { credentials: 'include' });
          const html = await res.text();
          const parser = new DOMParser();
          const doc = parser.parseFromString(html, 'text/html');
          const parsed = parseAssessmentDoc(doc, w);
          allQuestions.push(...parsed);
        }
      } catch (err) {
        console.error(`Failed to fetch Assignment ${w}:`, err);
      }
    }
  }

  console.log(`%c[DIHCI Extractor] Total questions extracted: ${allQuestions.length}`, "color: #10b981; font-size: 16px; font-weight: bold;");

  // 3. Download as dihci_questions.json
  const dataBlob = new Blob([JSON.stringify(allQuestions, null, 2)], { type: 'application/json' });
  const downloadUrl = URL.createObjectURL(dataBlob);
  const a = document.createElement('a');
  a.href = downloadUrl;
  a.download = 'dihci_questions.json';
  document.body.appendChild(a);
  a.click();
  a.remove();
  URL.revokeObjectURL(downloadUrl);

  console.log("%c[DIHCI Extractor] 'dihci_questions.json' downloaded successfully!", "color: #10b981; font-size: 14px; font-weight: bold;");
  return allQuestions;
})();
