n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def f(n):
    if (n == 0):
        return arr[0]
    # 현재까지의 최소공배수와 arr[n]간에 최대공약수를 구하고 그 arr[n] //최대공약수만큼을 곱해주기
    if (f(n-1) % arr[n] != 0):
        for i in range(arr[n], 0, -1):
            if (f(n-1)%i == 0) & (arr[n]%i == 0):
                # print(f"n = {n}, f(n-1) * arr[n]//i = {f(n-1) * (arr[n]//i)}")
                return f(n-1) * (arr[n]//i)
        # return f(n-1) * arr[n]
    else:
        return f(n-1)


print(f(n-1))