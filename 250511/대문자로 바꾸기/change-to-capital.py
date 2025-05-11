import string

arr = []

for _ in range(5):
    temp = list(input().split().upper())
    arr.append(temp)

print(*arr)