a, b = map(int, input().split())

# Please write your code here.
def a_b(a, b):
    ans = 1
    for _ in range(b):
        ans *= a
    return ans


print(a_b(a, b))    