n = int(input())
ans = []

for i in range(1, n+1):
    tmp = []
    for j in range(1, i+1):
        if (i%j==0):
            tmp.append(j)
    if (len(tmp)==2):
        ans.append(tmp[1])
print(*ans)