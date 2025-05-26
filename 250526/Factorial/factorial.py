N = int(input())

# Please write your code here.
def fac(n):
    if (n==0):
        return 1
    return fac(n-1) * n


print(fac(N))