s = []

while (1):
    given = input()
    if (given == '0'):
        break
    s.append(given)

print(len(s))
for i in range(len(s)):
    if (i%2==0):
        print(s[i])