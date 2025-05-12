arr = [[0 for _ in range(5)] for _ in range(5)]

for i in range(5):
    for j in range(5):
        if (i==0) | (j==0):
            arr[i][j] = 1
        else:
            arr[i][j] = arr[i-1][j] + arr[i][j-1]

for i in range(5):
    print(*arr[i])