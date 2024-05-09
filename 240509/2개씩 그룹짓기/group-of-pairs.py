N = int(input())

arr = list(map(int, input().split()))
arr.sort()
#print(arr)

arr_sum = []

for i in range(N):
    if i == N:
        break
    sum = arr[i] + arr[2*N-1-i]
    arr_sum.append(sum)
    #print("i = ", i)
    #print("sum : ", sum)

print(max(arr_sum))