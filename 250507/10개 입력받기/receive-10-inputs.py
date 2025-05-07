arr = list(map(int, input().split()))
s = []

for i in arr:
    if (i==0):
        break
    else:
        s.append(i)

print(sum(s), round(sum(s)/len(s), 1))