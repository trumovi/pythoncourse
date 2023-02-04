def palindrom():
    line = str(input())
    a = line[::-1]
    if line == a:
        print("yes")
    else:
        print("no")


palindrom()