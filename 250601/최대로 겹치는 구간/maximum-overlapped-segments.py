n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = [0] * 100
for seg in segments:
    for i in range(seg[0], seg[1]):
        ans[i] += 1

print(max(ans))