n = int(input())
ans = []
cnt = 0

for i in range(n):
    score = list(map(int, input().split()))
    if (sum(score)/len(score) >= 60):
        ans.append('pass')
        print('pass')
    else:
        ans.append('fail')
        print('fail')

for i in ans:
    if (i == 'pass'):
        cnt += 1
    
print(cnt)