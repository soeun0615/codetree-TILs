n = int(input())
m = n if (n%2==0)|(n==1) else n-1

for i in range(m):
    for j in range(n):
        if (i==0):
            print("*", end=" ")
        else:
            if (j%2==1)&(j>=i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
