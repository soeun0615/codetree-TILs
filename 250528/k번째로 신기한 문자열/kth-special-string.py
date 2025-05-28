n, k, t = input().split()
n, k = int(n), int(k)
word = [input() for _ in range(n)]

# Please write your code here.
list_t = [word[i] for i in range(n) if word[i][:len(t)] == t]
list_t.sort()
print(list_t[k-1])