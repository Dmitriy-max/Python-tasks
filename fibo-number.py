def chekNumber():
    number = int(input('Enter a number from 0 to 9999> '))
    fiboRow = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765] 
    if number in fiboRow:
        print('YES')
    else:
        print("NO")

chekNumber()
