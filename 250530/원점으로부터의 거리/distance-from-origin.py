n = int(input())
points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]

# Please write your code here.
points.sort(key = lambda x:abs(x[1][0]) + abs(x[1][1]))
for p in points:
    print(p[0])