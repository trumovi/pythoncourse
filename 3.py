def number():
    a = input('number: ')
    sum = 0
    for i in a:
        sum += int(i)
    return sum


number()