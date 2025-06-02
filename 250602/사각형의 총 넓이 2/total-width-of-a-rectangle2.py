n = int(input())

# Please write your code here.
ans = [([0]*200) for _ in range(200)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = x1 + 100, y1 + 100, x2 + 100, y2 + 100
    for i in range(x1, x2):
        for j in range(y1, y2):
            ans[i][j] = 1
            # print(f"i = {i}, j = {j}, ans[i][j] = {ans[i][j]}")
            
cnt = 0
for i in range(200):
    for j in range(200):
        if (ans[i][j] == 1):
            cnt += 1
print(cnt)