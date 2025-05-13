n = int(input())
arr = [input() for _ in range(n)]
word = input()

ans = []
sum_v = 0

for w in arr:
    if (w[0] == word):
        ans.append(w)
        sum_v += len(w)

print(f"{len(ans)} {sum_v / len(ans):.2f}")