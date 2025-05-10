import sys

n = int(input())
nums = list(map(int, input().split()))

gap = sys.maxsize

for i in range(n):
    for j in range(n):
        if (abs(nums[i] - nums[j]) < gap) & (abs(nums[i] - nums[j]) != 0):
            gap = abs(nums[i] - nums[j])

print(gap)