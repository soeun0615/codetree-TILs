sent, w = input().split()

ans = 0
if (sent.find(w)==-1):
    ans = "No"
else:
    ans = sent.find(w)

print(ans)