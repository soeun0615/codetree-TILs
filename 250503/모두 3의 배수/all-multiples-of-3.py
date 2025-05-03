sat = False
for i in range(5):
    n = int(input())

    if (n%3==0):
        continue
    else:
        sat = True
        break

if (sat == False):
    print(1)
else:
    print(0)