n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]
num = 0

for j in range(m):
    for i in range(n):
        if (j%2==0):
            arr[i][j] = num
        else:
            arr[n-i-1][j] = num
        num += 1

for i in range(n):
    print(*arr[i])