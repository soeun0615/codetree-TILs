arr = [input() for _ in range(10)]
word = input()
ans = []

for w in arr:
    if (w[-1] == word):
        ans.append(w)

if (len(ans) == 0):
    print("None")
else:
    print(*ans, sep="\n")