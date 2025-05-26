N = int(input())

# Please write your code here.
def f(n):
    if (n == 1)|(n == 2):
        return 1
    return f(n-1) + f(n-2)


print(f(N))