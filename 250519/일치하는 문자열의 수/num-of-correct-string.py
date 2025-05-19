n, A = input().split()

cnt = 0
for _ in range(int(n)):
    tmp = input()
    if (tmp == A):
        cnt += 1

print(cnt)