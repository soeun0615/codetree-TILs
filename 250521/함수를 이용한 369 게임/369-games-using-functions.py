a, b = map(int, input().split())

# Please write your code here.
def count_3(n):
    num = list(str(n))
    if (n%3==0):
        return True
    elif ('3' in num) | ('6' in num) | ('9' in num):
        return True
    else:
        return False

def count_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if (count_3(i) == True):
            cnt += 1
    return cnt


print(count_num(a, b))