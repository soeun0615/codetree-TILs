cnt1, cnt2 = 0, 0
l = []

for i in range(10):
    l.append(int(input()))
    if (l[i]%3==0):
        cnt1 = cnt1 + 1
    if (l[i]%5==0):
        cnt2 = cnt2 + 1

print(cnt1, cnt2)