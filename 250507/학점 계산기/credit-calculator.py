n = int(input())
score = list(map(float, input().split()))

ans = round(sum(score)/n, 1)
print(ans)

if (ans >= 4.0):
    print("Perfect")
elif (ans >= 3.0):
    print("Good")
else:
    print("Poor")