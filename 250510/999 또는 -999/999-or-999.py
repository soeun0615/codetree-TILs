arr = list(map(int, input().split()))

for i, elem in enumerate(arr):
    if (abs(elem) == 999):
        filtered_arr = arr[:i]

print(max(filtered_arr), min(filtered_arr))