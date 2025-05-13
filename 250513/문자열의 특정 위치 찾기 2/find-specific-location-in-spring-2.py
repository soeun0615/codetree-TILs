word = ["apple", "banana", "grape", "blueberry", "orange"]
given = input()
ans = []

for w in word:
    if (given == w[2]) | (given == w[3]):
        ans.append(w)

if (len(ans)>0):
    print(*ans, sep = "\n")
print(len(ans))