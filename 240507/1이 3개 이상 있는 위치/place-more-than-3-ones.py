N = int(input())
A = [
    list(map(int, input().split()))
    for _ in range(N)
]

dxs = [0, 0, -1, 1]
dys = [1, -1, 0, 0]

def in_range(x, y):
    return 0 <= x < N and 0 <= y < N

answer = 0
for i in range(N):
    for j in range(N):
        cnt = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and A[nx][ny] == 1:
                cnt += 1
        if cnt >= 3:
            answer += 1

print(answer)