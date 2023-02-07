def palindrom():
    line = str(input())
    a = line[::-1]
    if line == a:
        return True
    else:
        return False


palindrom()