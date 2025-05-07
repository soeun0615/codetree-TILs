n = int(input())
arr = list(map(int, input().split()))
arr2 = []
ans = []

for a in arr:
    if (a%2==0):
        arr2.append(a)

ans = reversed(arr2)
print(*ans)