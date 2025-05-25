n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.
def div_add():
    global m, A
    ans = A[m-1]
    while (m != 1):
        if (m % 2 == 1):
            m -= 1
        else:
            m //= 2
        ans += A[m-1]
    return ans


ans = div_add()
print(ans)    