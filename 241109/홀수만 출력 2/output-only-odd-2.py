b, a = map(int, input().split())
# print('a = ', a)
# print('b = ', b)

for i in range(b, a-1, -1):
    if i%2==1:
        print(i, end=' ')