n = int(input())

# Please write your code here.
def ans(n):
    if (n%2==0) & (((n//10) + (n%10))%5==0):
        print('Yes')
    else:
        print('No')

    
ans(n)