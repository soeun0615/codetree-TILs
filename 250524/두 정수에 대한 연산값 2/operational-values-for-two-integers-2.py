a, b = map(int, input().split())

# Please write your code here.
def mod_ab(a, b):
    if (a>b):
        a *= 2
        b += 10
    else:
        a += 10
        b *= 2
    return a, b


a, b = mod_ab(a, b)
print(a, b)