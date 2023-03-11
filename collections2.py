import collections
import json

with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
chars = collections.defaultdict(list)
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for hap in action['says']:
                # print(action['character'])
                chars[action['character']].append(hap)
# print(chars)
with open('characters.json','w') as w:
    json.dump(chars, w, ensure_ascii=False, indent=4)
