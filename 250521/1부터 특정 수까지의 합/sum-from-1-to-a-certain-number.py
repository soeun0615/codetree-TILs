n = int(input())

# Please write your code here.
def sum_10(n):
    sum_val = sum([i for i in range(1, n+1)])
    ans = sum_val//10
    return ans

print(sum_10(n))