n = int(input())
answer = []

for i in range(1, n+1):
    if (i%2==0):
        continue
    if (i%10==5):
        continue
    if (i%3==0) & (i%9!=0):
        continue
    print(i, end=' ')