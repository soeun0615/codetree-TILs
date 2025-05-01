n = int(input())
answer = [n]

for i in range(1, n):
    m = answer[i-1]//i
    answer.append(m)
    if (m<=1):
        print(len(answer)-1)
        break