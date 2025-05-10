arr = list(map(int, input().split()))
arr_u = []
arr_o = []

for elem in arr:
    if (elem < 500):
        arr_u.append(elem)
    else:
        arr_o.append(elem)

print(max(arr_u), min(arr_o))