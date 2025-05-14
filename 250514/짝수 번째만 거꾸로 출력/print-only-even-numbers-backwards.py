word = input()

ans = []
for i in range(len(word)):
    if (i%2==1):
        ans.append(word[i])

for i in range(len(ans)-1, -1, -1):
    print(ans[i], end="")