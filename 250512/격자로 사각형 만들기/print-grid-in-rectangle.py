n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if (i==0)|(j==0):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j] + arr[i][j-1]

for i in range(n):
    print(*arr[i])