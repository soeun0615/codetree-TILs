import string

arr = []

for _ in range(5):
    temp = list(input().split())
    arr.append(temp)

for i in range(5):
    for j in range(3):
        print(arr[i][j].upper(), end=' ')
    print()
