a, b, c, d = map(int, input().split())

# Please write your code here.
time_ab = (a * 60) + b * 1
time_cd = (c * 60) + d * 1

# print(time_ab, time_cd)
print(abs(time_ab - time_cd))