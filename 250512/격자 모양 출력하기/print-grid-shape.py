n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    r, c = map(int, input().split())
    arr[r-1][c-1] = r * c

for i in range(n):
    print(*arr[i])
