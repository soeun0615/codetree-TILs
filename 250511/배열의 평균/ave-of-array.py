avg_h = []
avg_v = []

arr = [list(map(int, input().split())) for _ in range(2)]

for i in range(2):
    avg_h.append(sum(arr[i])/len(arr[i]))

for j in range(4):
    sum_v = 0
    for i in range(2):
        sum_v += arr[i][j]
    avg_v.append(sum_v/len(arr))

w_avg = (sum(avg_h)+sum(avg_v))/(len(avg_h)+len(avg_v))
print(*avg_h)
print(*avg_v)
print(round(w_avg, 1))