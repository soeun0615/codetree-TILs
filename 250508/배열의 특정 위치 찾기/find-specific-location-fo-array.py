arr = list(map(int, input().split()))

arr_even = arr[1::2]
arr_3 = arr[2::3]

print(sum(arr_even), round(sum(arr_3)/len(arr_3), 1))