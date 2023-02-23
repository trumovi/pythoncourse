import json

defs = []
with open('wikidata_1000.json', 'r', encoding="utf-8") as d:
    for opr in d:
        defs.append(json.loads(opr))

info = {}
for line in defs:
    if "description" in line:
        info[line["label"]["value"]] = line['description']["value"]
    else:
        info[line["label"]["value"]] = "None"

with open("wiki.json", "w", encoding="utf-8") as g:
    json.dump(info, g, ensure_ascii=False, indent=4)
