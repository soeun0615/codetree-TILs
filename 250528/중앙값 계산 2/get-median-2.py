n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    if (i%2==0):
        temp = arr[:i+1]
        temp.sort()
        print(temp[i//2], end=" ")