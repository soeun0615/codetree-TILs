n, m = map(int, input().split())

# Please write your code here.
arr = [[0 for _ in range(m)] for _ in range(n)]
num, i, j = 1, 0, 0

for s in range(0, n+m-1):
    if (s < m):
        i, j = 0, s
    else:
        i, j = (s-m+1), m-1
    # print(f"s = {s}")
    # print(f"i, j = {i}, {j}")
    while (i+j==s) & (0 <= i < n) & (0 <= j < m):
        arr[i][j] = num
        # print(f"arr[{i}][{j}] = {num}")
        num += 1
        i += 1
        j -= 1

for i in range(n):
    print(*arr[i])

# print(f"arr[{i}][{tmp}] = {num}")