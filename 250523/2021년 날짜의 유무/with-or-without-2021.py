M, D = map(int, input().split())

# Please write your code here.
def date_ex(M, D):
    month = [i for i in range(1, 13)]
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = 'No'
    if (M in month):
        i = month.index(M)
        if (D <= day[i]):
            ans = 'Yes'
    print(ans)


date_ex(M, D)