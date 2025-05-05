n = int(input())
cnt = 1

for i in range(n):
    for j in range(n):
        if (cnt==5):
            cnt = 1
        print(2*cnt, end=" ")
        cnt += 1
    print()