n = int(input())
price = list(map(int, input().split()))

# Please write your code here.
gap = 0
for i in range(n):
    for j in range(i, n):
        if (price[j] - price[i] > gap):
            gap = price[j] - price[i]

print(gap)