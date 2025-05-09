n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = []
ans = 'Yes'

for i in range(n1):
    if (a[i] == b[0]) & ((n1-(i+1)-n2)>=0):
        idx.append(i)

for i in idx:
    tmp = a[i:i+n2]
    for j in range(n2):
        if (tmp[j]!=b[j]):
            ans = 'No'
            break

if (idx == []):
    ans = 'No'
    
print(ans)