A = input()
B = input()

cnt = 0
for i in range(1, len(A)+1):
    tmp = A[-i:] + A[:-i]
    cnt += 1
    if (tmp == B):
        break

if (cnt == len(A)):
    print(-1)
else:
    print(cnt)