n = int(input())
ans = []
cnt = 0

for i in range(n):
    score = list(map(int, input().split()))
    if (sum(score)/len(score) >= 60):
        ans.append('pass')
        print('pass')
        cnt += 1
    else:
        ans.append('fail')
        print('fail')
    
print(cnt)