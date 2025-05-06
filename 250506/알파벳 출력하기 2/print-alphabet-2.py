n = int(input())
cnt = 0

for i in range(n):
    for j in range(n):
        if (j<i):
            print(" ", end=" ")
        elif (chr(65+cnt) == 'Z'):
            print(chr(65+cnt), end=" ")
            cnt = 0
        else:
            print(chr(65+cnt), end=" ")
            cnt += 1
    print()
