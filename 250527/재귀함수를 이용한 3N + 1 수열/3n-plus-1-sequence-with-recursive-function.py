n = int(input())
cnt = 0
# Please write your code here.
def f(n):
    global cnt
    if (n == 1):
        return cnt

    cnt += 1
    if (n%2 == 0):
        return f(n//2)
    else:
        return f(3*n + 1)


print(f(n))