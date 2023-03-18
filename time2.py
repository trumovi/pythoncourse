import time
import json
import collections

start = time.time()
with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
chars = collections.defaultdict(list)
for act in data['acts']:
    for scene in act['scenes']:
        for action in scene['action']:
            for hap in action['says']:
                chars[action['character']].append(hap)
secs = str(time.time() - start)
file = time.strftime('%H.%M.%S %d.%m.%Y') + ".txt"
with open(file, "w", encoding="UTF-8") as d:
    d.write(secs)
