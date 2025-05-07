arr = list(map(int, input().split()))
s = []

for i in arr:
    if (i<250):
        s.append(i)
    else:
        break

print(sum(s), round(sum(s)/len(s), 2))