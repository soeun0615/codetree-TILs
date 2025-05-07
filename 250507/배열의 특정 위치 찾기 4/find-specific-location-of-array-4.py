arr = list(map(int, input().split()))
n = []
ans = []

for i in arr:
    if (i==0):
        break
    else:
        n.append(i)

for i in n:
    if (i%2==0):
        ans.append(i)

print(len(ans), sum(ans))
