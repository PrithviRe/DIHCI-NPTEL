import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

for q in questions:
    if q['id'] == 'w11_q5':
        # Prompt: In ____________, we assign some (arbitrary) codes to attributes of observational data.
        # Add option 'a': 'nominal'
        q['options'] = [
            {"id": "a", "text": "nominal"},
            {"id": "b", "text": "ordinal"},
            {"id": "c", "text": "interval"},
            {"id": "d", "text": "ratio"}
        ]
        q['correctAnswers'] = ["a"]
        q['explanation'] = (
            "**Why it's Correct:** Option A (nominal) is correct because assigning arbitrary numerical or symbolic codes "
            "to categories/attributes of observational data without any quantitative magnitude or intrinsic rank order "
            "(e.g., 1 = Male, 2 = Female, or 1 = Mouse, 2 = Touchpad) is the textbook definition of a Nominal Measurement Scale.\n\n"
            "**Why Other Options are Incorrect:** Ordinal data (Option B) represents ranked order (1st, 2nd, 3rd) without equal intervals. "
            "Interval data (Option C) has equal distances between points but an arbitrary zero point (like Celsius temperature). "
            "Ratio data (Option D) possesses a true absolute zero point (like task completion time in seconds or error count).\n\n"
            "**Course Context:** Stanley Smith Stevens (1946) established the four foundational levels of measurement: "
            "Nominal, Ordinal, Interval, and Ratio, which dictate what statistical tests (parametric vs. non-parametric) can be performed."
        )

    elif q['id'] == 'w11_q6':
        # Prompt: Recording data from a thermometer is an example of interval scaled data.
        # Add option 'a': 'True'
        q['options'] = [
            {"id": "a", "text": "True"},
            {"id": "b", "text": "False"}
        ]
        q['correctAnswers'] = ["a"]
        q['explanation'] = (
            "**Why it's Correct:** Option A (True) is correct because temperature measured on a standard thermometer "
            "(in degrees Celsius or Fahrenheit) is the quintessential textbook example of Interval Scaled Data. "
            "The distance between 10°C and 20°C is identical to that between 20°C and 30°C (equal intervals), but 0°C is an arbitrary "
            "reference freezing point, not the absolute absence of heat.\n\n"
            "**Why Other Options are Incorrect:** Option B (False) is incorrect because temperature scales (except Kelvin, which is ratio) "
            "fit the strict mathematical criteria of interval scale.\n\n"
            "**Course Context:** Understanding interval scales is crucial in HCI because subjective user ratings on Likert scales "
            "(e.g., SUS questionnaires from 1 to 5) are frequently treated as interval-level data for calculating means and standard deviations."
        )

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print("Successfully restored options for w11_q5 and w11_q6!")
