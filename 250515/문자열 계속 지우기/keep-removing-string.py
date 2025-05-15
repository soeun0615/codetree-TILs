A = input()
B = input()

# Please write your code here.
temp = list(A)
ind = A.find(B)

while (ind != -1):
    temp = A[:ind] + A[ind+len(B):]
    A = ''.join(temp)
    ind = A.find(B)

print(A)