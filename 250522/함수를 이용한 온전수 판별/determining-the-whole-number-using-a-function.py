a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        if (i%2 == 0):
            continue
        elif (i%10 == 5):
            continue
        elif (i%3==0) & (i%9 != 0):
            continue
        else:
            cnt += 1
    return cnt


print(find_num(a, b))