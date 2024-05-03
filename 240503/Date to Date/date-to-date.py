num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

gap1 = 0
for i in range(m1):
    gap1 += num_of_days[i-1]

gap1 += d1

gap2 = 0
for i in range(m2):
    gap2 += num_of_days[i-1]

gap2 += d2

gap = gap2-gap1
print(gap)