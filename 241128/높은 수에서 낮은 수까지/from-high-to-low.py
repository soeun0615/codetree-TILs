a, b = map(int, input().split())

for i in range(abs(a-b-1)):
    print(max(a, b)-i, end=' ')