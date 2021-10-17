number = 5
for i in range(number, 0, -1):
    num = i
    for j in range(0, i):
        print(num, end=' ')
    print("\r")