import json


with open('RomeoAndJuliet.json', 'r', encoding='UTF-8') as d:
    data = json.load(d)
chars = {}
for act in data["acts"]:
    for scene in act["scenes"]:
        for action in scene["action"]:
            if action["character"] not in chars:
                chars[action["character"]] = 1
            else:
                chars[action["character"]] += 1

max = 0
for character in chars:
    if chars[character] >= max:
        max = chars[character]
        name = character
print(name)
