a, b = map(int, input().split())

c = []
for i in range(b, a-1, -1):
    if (i%2==0):
        c.append(i)

for i in range(9):
    for j in c:
        if (j%2==0):
            print(f"{j} * {i+1} = {j * (i+1)}", end=" ")

        if (j!=c[len(c)-1]):
            print("/", end=" ")
    print()