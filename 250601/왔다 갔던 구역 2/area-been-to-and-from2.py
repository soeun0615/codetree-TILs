n = int(input())
x = []
directs = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    directs.append(di)

# Please write your code here.
ans = [0] * sum(x) * 2
now = sum(x)

for i in range(n):
    if (i != 0):
        if (directs[i] == directs[i-1]):
            # print(f"변경 전 : now = {now}, ans[now] = {ans[now]}")
            ans[now] -= 1
            # print(f"변경 후 :now = {now}, ans[now] = {ans[now]}")

    if (directs[i] == 'L'):
        for j in range(now, now-x[i]-1, -1):
            ans[j] += 1
        now -= x[i]
    else:
        for j in range(now, now+x[i]+1, 1):
            ans[j] += 1
        now += x[i]
    # print(f"i = {i}, x[i] = {x[i]}, now = {now}")
# print(ans)
cnt = 0
for i in range(len(ans)):
    if (ans[i]>=2) & (ans[i+1]>=2):
        cnt += 1
        # print(f"ans[{i}] = {ans[i]}, cnt = {cnt}")
    if (ans[i] == 0) & (cnt > 0):
        break
print(cnt)
