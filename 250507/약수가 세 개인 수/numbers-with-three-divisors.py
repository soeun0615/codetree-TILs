start, end = map(int, input().split())
cnt = 0

# Please write your code here.
for i in range(start, end+1):
    ans = []
    for j in range(1, i+1):
        if (i%j==0):
            ans.append(j)
        else:
            continue
        
    if (len(ans)==3):
        cnt += 1

print(cnt)