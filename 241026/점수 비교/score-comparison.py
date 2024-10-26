A_m, A_e = map(int, input().split())
B_m, B_e = map(int, input().split())

if (A_m > B_m) and (A_e > B_e):
    print(1)
else:
    print(0)