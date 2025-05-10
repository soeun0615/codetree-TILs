import sys

n = int(input())
arr = list(map(int, input().split()))
min_val = sys.maxsize

# Please write your code here.
for elem in arr:
    if (elem < min_val):
        min_val = elem

print(min_val, arr.count(min_val))