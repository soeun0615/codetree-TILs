N = int(input())

# Please write your code here.
def sum_val(n):
    if (n == 1):
        return 1
    return sum_val(n-1) + n


print(sum_val(N))    