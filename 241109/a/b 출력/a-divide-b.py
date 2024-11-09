import math
a, b = map(int, input().split())

ans = []
print(f'{a//b}.', end='')
for _ in range(20):
    a*=10
    ans.append(a//b)

print(ans[-1])