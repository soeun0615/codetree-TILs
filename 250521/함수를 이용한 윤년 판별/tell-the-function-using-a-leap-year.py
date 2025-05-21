y = int(input())

# Please write your code here.
def find_leap(y):
    if (y%100 == 0) & (y%400 != 0):
        return False
    if (y%4==0):
        return True
    return False


if (find_leap(y) == True):
    print('true')
else:
    print('false')