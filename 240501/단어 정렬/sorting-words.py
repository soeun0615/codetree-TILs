n = int(input())
arr = [input() for _ in range(n) ]

sorted_arr = sorted(arr)

print(*sorted_arr, sep="\n")