import json
import collections


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
cnt = collections.Counter()
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            for line in action["says"]:
                cnt[action['character']] += 1


print(cnt)
