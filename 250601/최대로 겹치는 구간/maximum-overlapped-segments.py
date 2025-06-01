n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ans = [0] * 200
for seg in segments:
    for i in range(seg[0]+100, seg[1]+100):
        ans[i] += 1

print(max(ans))