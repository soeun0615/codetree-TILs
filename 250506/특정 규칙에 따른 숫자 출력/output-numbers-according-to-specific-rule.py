n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        if (j<i):
            print(" ", end=" ")
        elif (cnt == 9):
            cnt = 1
            print(cnt, end=" ")
        else:
            cnt += 1
            print(cnt, end=" ")
    print()