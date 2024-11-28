a, b = map(int, input().split())
i = a

print(i, end=' ')
while(i<=b):
    if i%2==1: i = i*2
    else: i = i+3

    if i>b: break
    print(i, end=' ')