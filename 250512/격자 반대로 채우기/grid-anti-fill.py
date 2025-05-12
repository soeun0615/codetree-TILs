n = int(input())

arr = [[0 for _ in range(n)] for _ in range(n)]
num = 1

for j in range(n-1, -1, -2):
    for i in range(n-1, -1, -1):
        arr[i][j] = num
        num += 1

    j -= 1
    if (j<0):
        break

    for i in range(n):
        arr[i][j] = num
        num += 1

for i in range(n):
    print(*arr[i])