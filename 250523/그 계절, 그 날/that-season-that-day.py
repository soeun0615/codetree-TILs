Y, M, D = map(int, input().split())

# Please write your code here.
def find_season(Y, M, D):
    month = [i for i in range(1, 13)]
    day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (Y%4==0):
        day[1] = 29
    if (Y%4==0) & (Y%100==0):
        day[1] = 28
    if (Y%4==0) & (Y%100==0) & (Y%400==0):
        day[1] = 29

    ans = -1

    if (M in month):
        i = month.index(M)
        if (D <= day[i]):
            ans = 1
    
    if (ans == 1):
        if (3 <= int(M) <= 5):
            print('Spring')
        elif (6 <= int(M) <= 8):
            print('Summer')
        elif (9 <= int(M) <= 11):
            print('Fall')
        else:
            print('Winter')
    else:
        print(-1)


find_season(Y, M, D)        