m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.
days_of_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

days_1 = sum(days_of_month[:m1]) + d1
days_2 = sum(days_of_month[:m2]) + d2

ans = abs(days_1 - days_2) + 1

# print(days_1, days_2)
print(ans)