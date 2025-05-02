sum_val = 0
cnt = 0

while True:
    n = int(input())
    if ((n//10) == 2):
        sum_val += n
        cnt += 1
    else:
        break

s = sum_val/cnt
print(f"{s:0.2f}")