import json

with open('src/data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for q in data:
    q['prompt'] = q['prompt'].replace('\ufffd', "'")
    for opt in q['options']:
        opt['text'] = opt['text'].replace('\ufffd', "'")

with open('src/data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print('Sanitization complete!')
