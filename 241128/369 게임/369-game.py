n = int(input())

i = 1
while(i<=n):
    if i%3==0: print(0, end=' ')
    elif ((list(str(i)).count('3') + list(str(i)).count('6') + list(str(i)).count('9')) >0): print(0, end=' ')
    else: print(i, end=' ')
    i+=1