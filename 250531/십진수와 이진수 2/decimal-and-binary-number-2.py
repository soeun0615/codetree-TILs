N = list(map(int, input()))

# Please write your code here.
# 10진수로 변환
N_10 = 0
for i in range(len(N)):
    N_10 = N_10 * 2 + N[i]

# 17을 곱하고 다시 이진수로 변환
N_10 *= 17

N_2 = []
while True:
    if (N_10 < 2):
        N_2.append(N_10)
        break
    N_2.append(N_10%2)
    N_10 //= 2

for n in N_2[::-1]:
    print(n, end="")