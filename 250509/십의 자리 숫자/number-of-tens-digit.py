arr = list(map(int, input().split()))
filterd_arr = [arr[i]//10 for i in range(len(arr)) if (arr[i]!=0)]

arr_10 = [0] * 10

for elem in filterd_arr:
    arr_10[elem] += 1

for i in range(1, 10):
    print(f"{i} - {arr_10[i]}")