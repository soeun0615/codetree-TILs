n = int(input())
arr = [1, n]
i = 2

while True:
    arr.append(arr[i-1] + arr[i-2])
    i += 1
    if (arr[-1]>100):
        break

print(*arr)