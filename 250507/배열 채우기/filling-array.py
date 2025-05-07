score = list(map(int, input().split()))
s = []

for i in score:
    if (i==0):
        break
    else:
        s.append(i)

s1 = reversed(s)
print(*s1)