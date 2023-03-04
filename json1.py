import json

info = {}
with open('wikidata_1000.json', 'r', encoding="utf-8") as d:
    for line in d:
        defs = json.loads(line)
        key = defs["label"]["value"]
        if 'description' in line:
            value = defs["description"]['value']
        else:
            value = None
        info[key] = value


with open("wiki.json", "w", encoding="utf-8") as g:
    json.dump(info, g, ensure_ascii=False, indent=4)
