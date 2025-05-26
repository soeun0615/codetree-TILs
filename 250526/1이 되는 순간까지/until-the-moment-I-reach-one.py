N = int(input())
cnt = 0
# Please write your code here.
def f(n):
    global cnt
    if (n == 1):
        return cnt

    if (n%2==0):
        cnt += 1
        return f(n//2)
    else:
        cnt += 1
        return f(n//3)


print(f(N))