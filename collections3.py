import json
from collections import Counter


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
chars = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in chars:
                chars[action["character"]] = 1
            else:
                chars[action["character"]] += len(action['says'])

counts = Counter(chars)
print(counts)
