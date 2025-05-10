n = int(input())
arr = list(map(int, input().split()))

ans = []
# Please write your code here.
while len(arr)>=1:
    max_ind = arr.index(max(arr))
    ans.append(max_ind+1)

    arr = arr[:max_ind]
print(*ans)