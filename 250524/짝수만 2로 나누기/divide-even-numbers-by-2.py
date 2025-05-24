n = int(input())
_list = list(map(int, input().split()))

# Please write your code here.
def modify(arr):
    ans = []
    for i in range(len(arr)):
        if (arr[i]%2 == 0):
            ans.append(arr[i]//2)
        else:
            ans.append(arr[i])
    return ans


ans = modify(_list)
print(*ans)