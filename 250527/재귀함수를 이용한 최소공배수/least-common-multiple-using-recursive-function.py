n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n):
    if (n == 0):
        return arr[0]

    if (f(n-1) % arr[n] != 0):
        # print(f"n = {n}, f(n-1) * arr[n] = {f(n-1) * arr[n]}")
        return f(n-1) * arr[n]
    else:
        return f(n-1)


print(f(n-1))