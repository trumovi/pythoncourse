import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
info = []
for act in data["acts"]:
    for scene in act["scenes"]:
        chars = []
        for action in scene["action"]:
            chars.append(action["character"])
        info.append(list(set(chars)))

with open('randj.json', 'w') as d:
    for line in info:
        d.write(json.dumps(line, ensure_ascii=False, separators=(',', ':')))
        d.write("\n")
