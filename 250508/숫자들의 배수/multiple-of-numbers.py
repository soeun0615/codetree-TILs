n = int(input())
arr = []
cnt = 0

for i in range(10):
    arr.append(n * (i+1))
    if ((n * (i+1))%5==0):
        cnt += 1
    if (cnt == 2):
        break

print(*arr)