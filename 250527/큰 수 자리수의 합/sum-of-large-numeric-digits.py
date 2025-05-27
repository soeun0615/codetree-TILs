a, b, c = map(int, input().split())

# Please write your code here.
def add_num(arr, i):
    if (i == 0):
        return arr[0]
    return add_num(arr, i-1) + arr[i]

def f(a, b, c):
    arr = list(map(int, str(a*b*c)))
    ans = add_num(arr, len(arr)-1)
    return ans


print(f(a, b, c))