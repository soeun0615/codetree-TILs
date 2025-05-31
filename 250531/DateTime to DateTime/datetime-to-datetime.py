a, b, c = map(int, input().split())

# Please write your code here.
min_11 = (11 * 24 * 60) + (11 * 60) + 11
min_n = (a * 24 * 60) + (b * 60) + c

ans = min_n - min_11

if (min_n < min_11):
    ans = -1

print(ans)