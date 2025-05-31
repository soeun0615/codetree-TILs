m1, d1, m2, d2 = map(int, input().split())
A = input()

# Please write your code here.
day_of_month = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

A_i = day_of_week.index(A)
day_1 = sum(day_of_month[:m1]) + d1
day_2 = sum(day_of_month[:m2]) + d2

day_ans = day_2 - day_1
# print(day_ans)
# print(day_ans - A_i)

if (day_ans//7) == ((day_ans-A_i)//7):
    ans = (day_ans // 7) + 1
else:
    ans = day_ans // 7

print(ans)