n = int(input())

for i in range(n):
    for j in range(n):
        if (i==0):
            print(j+1, end=" ")
        elif (i%2==0):
            print(n*i+1+j, end=" ")
        else:
            print((i+1)*n-j, end=" ")
    print()