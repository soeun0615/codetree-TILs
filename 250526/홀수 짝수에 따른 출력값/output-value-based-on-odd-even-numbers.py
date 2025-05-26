N = int(input())

# Please write your code here.
def f(n):
    if (n <= 2):
        return n

    if (n % 2 == 1):
        return f(n-2) + n
    else:
        return f(n-2) + n


print(f(N))