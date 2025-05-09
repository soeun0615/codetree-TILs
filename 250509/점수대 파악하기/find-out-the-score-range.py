arr = list(map(int, input().split()))
filterd_arr = []
cnt_arr = [0] * 11

for i in range(len(arr)):
    if (arr[i]!=0):
        filterd_arr.append(arr[i]//10)
    else:
        break

for elem in filterd_arr:
    cnt_arr[elem] += 1

for i in range(10, 0, -1):
    print(f"{i * 10} - {cnt_arr[i]}")