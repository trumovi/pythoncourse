line = input()
myset = set(line)
if len(line) == len(myset):
    print("no duplicates")
else:
    print("there are duplicates")