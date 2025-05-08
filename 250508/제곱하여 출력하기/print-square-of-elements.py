n = int(input())
arr = list(map(int, input().split()))

new_arr = [elem * elem for elem in arr]
print(*new_arr)