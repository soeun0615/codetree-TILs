n = int(input())
cnt = 0

for i in range(n):
    for j in range(i+1):
        print(chr(65+cnt), end="")
        if (chr(65+cnt) == 'Z'):
            cnt = 0
        else:
            cnt += 1
    print()