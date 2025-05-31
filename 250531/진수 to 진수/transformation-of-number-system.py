a, b = map(int, input().split())
n = list(map(int, input()))

# Please write your code here.
n_10 = 0
for i in range(len(n)):
    n_10 = n_10 * a + n[i]

# print(n_10)
n_b = []
while True:
    if (n_10 < b):
        n_b.append(n_10)
        break
    n_b.append(n_10%b)
    n_10 //= b

for num in n_b[::-1]:
    print(num, end="")