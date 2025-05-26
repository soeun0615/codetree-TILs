n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n):
    global arr

    if (n == 0):
        return arr[0]

    return max(f(n-1), arr[n-1])


print(f(n))