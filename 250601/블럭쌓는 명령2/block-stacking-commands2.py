n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
ans = [0] * (n+1)

for cmd in commands:
    for i in range(cmd[0], cmd[1]+1):
        ans[i] += 1

print(max(ans))