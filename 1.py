def season():
    month = int(input("number: "))
    if month in [1, 2, 12]:
        print('winter')
    elif month in [3, 4, 5]:
        print('spring')
    elif month in [6, 7, 8]:
        print('summer')
    elif month in [9, 10, 11]:
        print('fall')

season()