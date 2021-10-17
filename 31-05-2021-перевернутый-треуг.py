n = 5
for i in range(n,0,-1):
    num = 1
    for j in range(n,0,-1):
        if j > i:
            print(" ", end=' ')
        else:
            print(num, end=' ')
            num += 1
    print("")