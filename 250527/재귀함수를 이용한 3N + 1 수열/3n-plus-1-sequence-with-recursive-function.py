n = int(input())

# Please write your code here.
def f(n):
    if (n == 1):
        return 0

    if (n%2 == 0):
        return f(n//2) + 1
    else:
        return f(3*n + 1) + 1


print(f(n))