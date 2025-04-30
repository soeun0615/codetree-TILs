sum_val, cnt = 0, 0

for i in range(10):
    n = int(input())
    if n in range(0, 201):
        sum_val += n
        cnt += 1

print(sum_val, round(sum_val/cnt, 1))