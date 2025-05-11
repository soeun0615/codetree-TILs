n, m = map(int, input().split())

arr = [
    [0 for _ in range(m)]
    for _ in range(n)
]

num = 0

for i in range(n):
    for j in range(m):
        num += 1
        arr[i][j] = num

for i in range(n):
    for j in range(m):
        print(arr[i][j], end=" ")
    print()