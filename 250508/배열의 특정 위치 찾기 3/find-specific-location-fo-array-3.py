arr = list(map(int, input().split()))
filterd_arr = []

for a in arr:
    if (a==0):
        break
    else:
        filterd_arr.append(a)

print(filterd_arr[-1] + filterd_arr[-2] + filterd_arr[-3])