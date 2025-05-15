given = input()
a, b = given[0], given[1]

s = list(given)
for i in range(len(s)):
    if (s[i] == a):
        s[i] = b
    elif (s[i] == b):
        s[i] = a

s = ''.join(s)
print(s)