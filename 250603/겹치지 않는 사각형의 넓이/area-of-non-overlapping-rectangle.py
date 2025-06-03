ans = [[0]*1000 for _ in range(1000)]

for _ in range(2):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            ans[i][j] = 1

# m넓이만큼을 빼기
x1, y1, x2, y2 = map(int, input().split())
for i in range(x1, x2):
    for j in range(y1, y2):
        ans[i][j] = 0

width = 0
for i in range(1000):
    for j in range(1000):
        if (ans[i][j] == 1):
            width += 1

print(width)