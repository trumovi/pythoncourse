import collections
import json
from collections import Counter

# cnt = collections.Counter()
with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
words = []
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for say in action['says']:
                # words.append(say)
                for line in say.split(' '):
                    words.append(line)

counts = Counter(words).most_common(20)
print(f"Most common:{counts}")
least_common = collections.Counter(words).most_common()[-21::]
print(f"Least common: {least_common}")
