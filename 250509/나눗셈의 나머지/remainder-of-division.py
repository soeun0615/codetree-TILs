a, b = map(int, input().split())
cnt_arr = [0] * b

while a>1:
    cnt_arr[a%b] += 1
    a = a//b

for i in range(len(cnt_arr)):
    cnt_arr[i] *= cnt_arr[i]

print(sum(cnt_arr))