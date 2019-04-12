def primoa(x):
    if x < 2:
        return False

    for i in range(2, x):
        if x % i == 0:
            return False
    return True


for a in range(1, 100):
    if primoa(a):
        print('É número primo', a)
