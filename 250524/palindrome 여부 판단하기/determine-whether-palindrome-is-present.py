A = input()

# Please write your code here.
def find_pnum(_str):
    tmp = [_str[i] for i in range(len(_str)//2)]
    r_tmp = [_str[-i] for i in range(1, len(_str)//2 + 1)]
    if (tmp == r_tmp):
        print('Yes')
    else:
        print('No')


find_pnum(A)