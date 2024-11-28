N = int(input())
int_list = []
for i in range(N):
    n = int(input())
    if (n%2==1) & (n%3==0):
        print(n)