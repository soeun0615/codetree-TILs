S, Q = input().split()
temp = list(S)

for _ in range(int(Q)):
    n, a, b = input().split()
    if (int(n) == 1):
        x, y = temp[int(a)-1], temp[int(b)-1]
        temp[int(a)-1] = y
        temp[int(b)-1] = x

    elif (int(n) == 2):
        for i in range(len(S)):
            if (temp[i] == a):
                temp[i] = b
    print(*temp, sep="")