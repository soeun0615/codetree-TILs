c, n = input().split()
n = int(n)

if c == 'A':
    for i in range(n):
        print(i+1, end=' ')
else:
    for i in range(n):
        print(n-i, end=' ')