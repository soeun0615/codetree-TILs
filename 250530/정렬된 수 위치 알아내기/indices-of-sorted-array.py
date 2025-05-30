n = int(input())
origin = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    origin[i] = (origin[i], int(i+1))

new = sorted(origin)
new_ind = [(int(i+1), new[i]) for i in range(n)]

new_ind.sort(key = lambda x:x[1][1])

for i in range(n):
    print(new_ind[i][0], end=" ")