n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

idx = []
ans = 'Yes'

for i in range(n1):
    if (a[i] == b[0]) & ((n1-(i+1)-n2)>=-1):
        idx.append(i)
# print(idx)

if (len(idx) == 0):
    ans = 'No'

for i in idx:
    tmp = a[i:i+n2]
    ans = 'Yes'
    # print(f"tmp = {tmp}")
    for j in range(n2):
        if (tmp[j]!=b[j]):
            # print(f"j = {j}")
            ans = 'No'
            break

print(ans)