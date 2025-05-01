n = int(input())
sum_val = 0

for i in range(n):
    m = int(input())
    sum_val += m

print(sum_val, round(sum_val/n, 1))