A = input()

# Please write your code here.
def find_alp(A):
    tmp = set(A)
    if (len(tmp) >= 2):
        print('Yes')
    else:
        print('No')


find_alp(A)