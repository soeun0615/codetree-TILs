given = list(input())

for i in range(len(given)-1):
    n = int(input())
    if (n >= len(given)):
        n = len(given)-1
    given.pop(n)
    print(*given, sep="")