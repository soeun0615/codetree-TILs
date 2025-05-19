n = int(input())

sum_val = 0
for _ in range(n):
    sum_val += int(input())

ans = str(sum_val)
print(ans[1:] + ans[0])