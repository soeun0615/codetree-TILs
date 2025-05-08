arr = list(map(int, input().split()))
sum_even, sum_odd = 0, 0

for i in range(len(arr)):
    if (i%2==0):
        sum_even += arr[i]
    else:
        sum_odd += arr[i]

print(abs(sum_even-sum_odd))