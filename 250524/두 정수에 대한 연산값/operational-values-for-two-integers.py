a, b = map(int, input().split())

# Please write your code here.
def modify(a, b):
    if (a>b):
        m = a + 25
        n = b * 2
    else:
        m = a * 2
        n = b + 25
    return m, n


m, n = modify(a, b)
print(m, n)