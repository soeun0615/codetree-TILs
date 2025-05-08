arr = list(map(int, input().split()))
ans = []

for i in range(len(arr)):
    if (arr[i]==0):
        break
    elif (arr[i]%2==0):
        ans.append(arr[i]//2)
    else:
        ans.append(arr[i] + 3)

print(*ans)
