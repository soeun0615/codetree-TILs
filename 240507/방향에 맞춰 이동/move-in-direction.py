n = int(input())

x, y = 0, 0
dx, dy = [1, 0, -1, 0], [0, -1, 0, 1]
dir_ro = ['E', 'S', 'W', 'N']

for _ in range(n):
    ind = 0
    dir_str, dist = input().split()
    num = int(dist)

    for i in range(len(dir_ro)):
        if dir_str == dir_ro[i]: ind = i

    x = x + dx[ind]*num
    y = y + dy[ind]*num

print(x, y)