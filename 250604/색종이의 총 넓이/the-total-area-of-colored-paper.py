n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
# x, y = zip(*points)
# x = [p[0]+100 for p in points]
# y = [p[1]+100 for p in points]

# Please write your code here.
ans = [[0]*200 for _ in range(200)]

for p in points:
    x = p[0] + 100
    y = p[1] + 100
    for i in range(x, x+8):
        for j in range(y, y+8):
            ans[i][j] = 1

cnt = 0
for i in range(200):
    for j in range(200):
        if (ans[i][j] == 1):
            cnt += 1

print(cnt)        