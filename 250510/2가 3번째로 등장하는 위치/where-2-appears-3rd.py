n = int(input())
arr = list(map(int, input().split()))

idx = []

for i in range(n):
    if (arr[i] == 2):
        idx.append(i+1)

print(idx[2])