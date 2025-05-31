m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
day_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day_of_week = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

day_1 = sum(day_of_month[:m1]) + d1
day_2 = sum(day_of_month[:m2]) + d2

day_ans = day_2 - day_1
print(day_of_week[day_ans % 7])
# if (-7 <= day_ans < 7):
#     print(day_of_week[day_ans])
# else:
#     print(day_of_week[day_ans % 7])

