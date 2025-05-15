sent = input()
ans = []

if ('ee' in sent):
    ans.append("Yes")
else:
    ans.append("No")
if ('ab' in sent):
    ans.append("Yes")
else:
    ans.append("No")

print(*ans)