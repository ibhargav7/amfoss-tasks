def compareTriplets(a, b):
    x = 0
    y = 0
    if a[0] > b[0]:
        x = x + 1
    elif a[0] < b[0]:
        y = y + 1
    elif a[0] == b[0]:
        pass
    if a[1] > b[1]:
        x = x + 1
    elif a[1] < b[1]:
        y = y + 1
    elif a[1] == b[1]:
        pass

    if a[2] > b[2]:
        x = x + 1
    elif a[2] < b[2]:
        y = y + 1
    elif a[2] == b[2]:
        pass
    return '{}{}'.format(x, y)