n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
max_val = max(arr)
arr.remove(max_val)
max_val2 = max(arr)

print(max_val, max_val2)