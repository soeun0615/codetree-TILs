start, end = map(int, input().split())
cnt = 0

# Please write your code here.
for i in range(start, end+1):
    ans = []
    for j in range(1, i):
        if (i%(j)==0):
            ans.append(j)
        else:
            continue
    if (sum(ans)==i):
        cnt += 1
print(cnt)