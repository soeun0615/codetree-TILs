n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
flt_arr = list(set(nums))
cnt_arr = [0] * len(flt_arr)

for elem in nums:
    i = flt_arr.index(elem)
    cnt_arr[i] += 1

max_val = -1
for i, elem in enumerate(cnt_arr):
    if (elem == 1):
        max_val = flt_arr[i]

print(max_val)