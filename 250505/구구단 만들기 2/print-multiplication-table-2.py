a, b = map(int, input().split())

for i in range(4):
    for j in range(b, a-1, -1):
        print(f"{j} * {2*(i+1)} = {j*2*(i+1)}", end=" ")

        if (j>a):
            print("/", end=" ")
    print()