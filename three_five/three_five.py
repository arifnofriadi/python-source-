for i in range(1, 101):
    if (i % 3 == 0) and (i % 5 == 0):
        print('three-five')
        continue
    elif (i % 3 == 0):
        print('three')
        continue
    elif (i % 5 == 0):
        print('five')
        continue
    else:
        print(i)