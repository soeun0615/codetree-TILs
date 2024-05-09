n = int(input())
A = list(map(int, input().split()))

answer = []

for i in range(n):
    S = 0
    for j in range(n):
        S += A[j] * abs(i-j)
    answer.append(S)
        #print("S : ", S)
    #answer = min(answer, S)
    #print("answer : ", answer)

print(min(answer))
'''
for i in range(5):
    A[i] *= 2
    S = 0
    for j in range(4):
        S += abs(A[j] - A[j+1])
    answer = max(answer, S)
    A[i] //= 2

print(answer)
'''