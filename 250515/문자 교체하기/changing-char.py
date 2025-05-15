given1, given2 = input().split()
tmp = list(given1)[:2]
s = list(given2)
s = tmp + s[2:]

print(*s, sep="")