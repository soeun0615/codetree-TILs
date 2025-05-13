n = int(input())
arr = [input() for _ in range(n)]

sum_v, cnt = 0, 0
for w in arr:
    sum_v += len(w)
    if (w[0] == 'a'):
        cnt += 1
print(sum_v, cnt)