n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

a = 0
for i in range(n):
    if A[i] == B[i]: 
        pass
    else :
        print("No")
        a = 1
        break

if a == 0:
    print("Yes")