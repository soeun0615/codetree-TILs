n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = []
ans = 'Yes'

for i in range(n1):
    if (a[i] == b[0]) & ((n1-(i+1)-n2)>=-1):
        idx.append(i)

if (len(idx) == 0):
    ans = 'No'

for i in idx:
    tmp = a[i:i+n2]
    if (tmp == b):
        ans = 'Yes'
        break
    else:
        ans = 'No'

print(ans)