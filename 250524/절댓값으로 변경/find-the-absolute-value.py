n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def arr_abs(arr):
    for i in range(len(arr)):
        arr[i] = abs(arr[i])


arr_abs(arr)
print(*arr)        