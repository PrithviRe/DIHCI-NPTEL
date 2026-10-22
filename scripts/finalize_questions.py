import json
import os

# 1. Load downloaded file (weeks 1 to 11)
downloads_path = os.path.expanduser('~\\Downloads\\dihci_questions.json')
with open(downloads_path, 'r', encoding='utf-8') as f:
    base_questions = json.load(f)

# Week 12 questions provided by user
w12_questions = [
  {
    "id": "w12_q1",
    "assignmentWeek": 12,
    "questionNumber": 1,
    "type": "single",
    "prompt": "With the significance test, we try to ______________ the null hypothesis.",
    "options": [
      { "id": "a", "text": "Accept" },
      { "id": "b", "text": "Refute" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w12_q2",
    "assignmentWeek": 12,
    "questionNumber": 2,
    "type": "single",
    "prompt": "Type I error is also known as ______________.",
    "options": [
      { "id": "a", "text": "False positive" },
      { "id": "b", "text": "False negative" },
      { "id": "c", "text": "True positive" },
      { "id": "d", "text": "True negative" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w12_q3",
    "assignmentWeek": 12,
    "questionNumber": 3,
    "type": "single",
    "prompt": "t-statistic is the ONLY way to test for statistical significance.",
    "options": [
      { "id": "a", "text": "True" },
      { "id": "b", "text": "False" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w12_q4",
    "assignmentWeek": 12,
    "questionNumber": 4,
    "type": "single",
    "prompt": "There are broadly two categories of the techniques for significance test: ______________ and ____________ .",
    "options": [
      { "id": "a", "text": "Parametric and Non-parametric" },
      { "id": "b", "text": "t-test and non t-test" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w12_q5",
    "assignmentWeek": 12,
    "questionNumber": 5,
    "type": "single",
    "prompt": "Project planning involves estimation of Project size, Cost, Duration and Effort.",
    "options": [
      { "id": "a", "text": "True" },
      { "id": "b", "text": "False" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w12_q6",
    "assignmentWeek": 12,
    "questionNumber": 6,
    "type": "single",
    "prompt": "COCOMO stands for ________________.",
    "options": [
      { "id": "a", "text": "Conducive Cost Estimation Model" },
      { "id": "b", "text": "Constructive Cost Estimation Model" },
      { "id": "c", "text": "Constructive Category Estimation Model" },
      { "id": "d", "text": "Conducive Category Estimation Model" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w12_q7",
    "assignmentWeek": 12,
    "questionNumber": 7,
    "type": "single",
    "prompt": "According to Boehm, software cost estimation should be done through ________________ stages.",
    "options": [
      { "id": "a", "text": "Two" },
      { "id": "b", "text": "Three" },
      { "id": "c", "text": "Four" },
      { "id": "d", "text": "Five" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w12_q8",
    "assignmentWeek": 12,
    "questionNumber": 8,
    "type": "single",
    "prompt": "Agile development ensure quick turn-around of projects",
    "options": [
      { "id": "a", "text": "True" },
      { "id": "b", "text": "False" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  },
  {
    "id": "w12_q9",
    "assignmentWeek": 12,
    "questionNumber": 9,
    "type": "single",
    "prompt": "Scrum is a _____________ method.",
    "options": [
      { "id": "a", "text": "Traditional SDLC" },
      { "id": "b", "text": "Agile" }
    ],
    "correctAnswers": ["b"],
    "explanation": "Official Accepted Answer: Option B"
  },
  {
    "id": "w12_q10",
    "assignmentWeek": 12,
    "questionNumber": 10,
    "type": "single",
    "prompt": "In a Gantt chart the length is proportional to ___________ for activity",
    "options": [
      { "id": "a", "text": "Duration planned" },
      { "id": "b", "text": "Effort" },
      { "id": "c", "text": "Cost" }
    ],
    "correctAnswers": ["a"],
    "explanation": "Official Accepted Answer: Option A"
  }
]

# Keep weeks 1 to 11 from base_questions, then append w12
all_final = [q for q in base_questions if q['assignmentWeek'] < 12]
all_final.extend(w12_questions)

# Clean options (remove any option that says "1 Point" or is duplicate)
for q in all_final:
    cleaned = []
    seen = set()
    for opt in q['options']:
        txt = opt['text'].strip()
        if txt.lower() in ['1 point', '2 points', 'point']:
            continue
        if opt['id'] not in seen and txt != '':
            seen.add(opt['id'])
            cleaned.append({'id': opt['id'], 'text': txt})
    q['options'] = cleaned

all_final.sort(key=lambda x: (x['assignmentWeek'], x['questionNumber']))

print(f"Total compiled questions: {len(all_final)}")
for w in range(1, 13):
    w_qs = [q for q in all_final if q['assignmentWeek'] == w]
    print(f"Week {w}: {len(w_qs)} questions | Q1: {w_qs[0]['prompt'][:40]}... (Ans: {w_qs[0]['correctAnswers']})")

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_final, f, indent=2)

print("Saved to src/data/questions.json successfully!")
