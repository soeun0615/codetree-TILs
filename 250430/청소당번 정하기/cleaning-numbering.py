n = int(input())
a, b, c = 0, 0, 0

a = n//2
b = n//3
c = n//12

if ((n//6) != 0):
    a = a-(n//6)

if ((n//12) != 0):
    b = b-(n//12)

print(a, b, c)
