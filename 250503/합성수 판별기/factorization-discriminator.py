n = int(input())
sat = False

for i in range(2, n):
    if (n%i==0):
        sat=True
        break

if (sat == True):
    print("C")
else:
    print("N")