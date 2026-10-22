import json

week2_raw = [
  {
    "id": "w2_q1",
    "assignmentWeek": 2,
    "questionNumber": 1,
    "type": "single",
    "prompt": "Contextual inquiry is also known as ___________.",
    "options": [
      { "id": "a", "text": "Interview" },
      { "id": "b", "text": "Observation" },
      { "id": "c", "text": "Semi-structured interview" }
    ],
    "correctAnswers": ["c"],
    "explanation": "Official Accepted Answer: Option C"
  },
  {
    "id": "w2_q2",
    "assignmentWeek": 2,
    "questionNumber": 2,
    "type": "single",
    "prompt": "In SRS, functions are not represented as",
    "options": [
      { "id": "a", "text": "Function name" },
      { "id": "b", "text": "Input" },
      { "id": "c", "text": "Output" },
      { "id": "d", "text": "Description" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w2_q3",
    "assignmentWeek": 2,
    "questionNumber": 3,
    "type": "single",
    "prompt": "Contextual inquiry can be done in _______ and passive mode.",
    "options": [
      { "id": "a", "text": "active" },
      { "id": "b", "text": "semi-active" },
      { "id": "c", "text": "neutral" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w2_q4",
    "assignmentWeek": 2,
    "questionNumber": 4,
    "type": "single",
    "prompt": "There are _______ stages in contextual inquiry.",
    "options": [
      { "id": "a", "text": "two" },
      { "id": "b", "text": "five" },
      { "id": "c", "text": "six" },
      { "id": "d", "text": "eight" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w2_q5",
    "assignmentWeek": 2,
    "questionNumber": 5,
    "type": "single",
    "prompt": "Which stage in the Contextual Inquiry process involves arranging for recording observations and scripting the procedure?",
    "options": [
      { "id": "a", "text": "Plan Stage" },
      { "id": "b", "text": "Initiate Stage" },
      { "id": "c", "text": "Execute Stage" },
      { "id": "d", "text": "Reflect Stage" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w2_q6",
    "assignmentWeek": 2,
    "questionNumber": 6,
    "type": "single",
    "prompt": "Affinity diagram method consists of _______ steps.",
    "options": [
      { "id": "a", "text": "Three" },
      { "id": "b", "text": "Two" },
      { "id": "c", "text": "Six" },
      { "id": "d", "text": "Five" }
    ],
    "correctAnswers": ["d"],
    "explanation": "Official Accepted Answer: Option D"
  },
  {
    "id": "w2_q7",
    "assignmentWeek": 2,
    "questionNumber": 7,
    "type": "single",
    "prompt": "Usability requirements is one type of ______.",
    "options": [
      { "id": "a", "text": "Functional Requirement" },
      { "id": "b", "text": "Non-functional requirement" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w2_q8",
    "assignmentWeek": 2,
    "questionNumber": 8,
    "type": "single",
    "prompt": "What is the primary objective of Contextual Inquiry?",
    "options": [
      { "id": "a", "text": "To watch and observe users perform tasks in their natural work setting" },
      { "id": "b", "text": "To conduct semi-structured interviews with users" },
      { "id": "c", "text": "To develop design recommendations" },
      { "id": "d", "text": "To study user behavior using physical note-taking" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w2_q9",
    "assignmentWeek": 2,
    "questionNumber": 9,
    "type": "single",
    "prompt": "What is the purpose of the \"Reflect\" stage in the Contextual Inquiry process?",
    "options": [
      { "id": "a", "text": "To contact the authorities for permission" },
      { "id": "b", "text": "To analyze the data collected and identify design goals" },
      { "id": "c", "text": "To script the procedure and rehearse for observations" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w2_q10",
    "assignmentWeek": 2,
    "questionNumber": 10,
    "type": "single",
    "prompt": "How long does the Contextual Inquiry process typically continue?",
    "options": [
      { "id": "a", "text": "One to two weeks" },
      { "id": "b", "text": "One to two hours" },
      { "id": "c", "text": "One to two months" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  }
]

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Replace week 2 questions
new_questions = []
for q in questions:
    if q['assignmentWeek'] == 2:
        continue
    new_questions.append(q)

new_questions.extend(week2_raw)
new_questions.sort(key=lambda x: (x['assignmentWeek'], x['questionNumber']))

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(new_questions, f, indent=2)

print(f"Updated questions.json! Total questions now: {len(new_questions)}")
