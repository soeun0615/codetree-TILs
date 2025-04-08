l = []
cnt = 0

for i in range(10):
    l.append(int(input()))
    if (l[i]%2 == 1):
        cnt = cnt+1

print(cnt)