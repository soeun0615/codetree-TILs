n = int(input())
arr = [[0 for _ in range(i+1)] for i in range(n)]

arr[0][0] = 1
for i in range(1, n):
    for j in range(i+1):
        if (j == 0):
            arr[i][j] = arr[i-1][j]
        elif (j == i):
            arr[i][j] = arr[i-1][j-1]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]

for i in range(n):
    print(*arr[i])