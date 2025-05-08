n = int(input())
arr = list(map(int, input().split()))
arr_even = []

for i in range(n):
    if (arr[i]%2==0):
        arr_even.append(arr[i])

print(*arr_even)