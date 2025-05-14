import string

A = input()

# Please write your code here.
cnt = 1
ans = []
for i in range(len(A)):
    if (i==0):
        ans.append(A[0])
        a = ans.index(A[i])
    elif (ans[a]==A[i]):
        cnt += 1
        if (i==len(A)-1):
            ans.append(cnt)
    else:
        ans.append(cnt)
        cnt = 1
        ans.append(A[i])
        a = ans.index(A[i])

temp = ""
for a in ans:
    s = str(a)
    temp += s
print(len(temp))
print(*ans, sep="")