n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
ans = 0
for i in range(n):
    if ((nums[i] + nums[2*n-i-1]) > ans):
        ans = nums[i] + nums[2*n-i-1]

print(ans)