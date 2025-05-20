n, m = map(int, input().split())

# Please write your code here.
def find_gcd(n, m):
    ans = 0
    for i in range(1, min(n, m)+1):
        if (n%i == 0) & (m%i == 0):
            ans = i
    print(ans)

find_gcd(n, m)