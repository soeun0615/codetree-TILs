A = input()
B = input()

cnt = 0
for i in range(len(A)-1):
    tmp = A[i:i+2]
    if (tmp == B):
        cnt += 1

print(cnt)