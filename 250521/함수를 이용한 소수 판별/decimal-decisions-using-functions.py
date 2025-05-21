a, b = map(int, input().split())

# Please write your code here.
def prime_num(a, b):
    ans = []
    for i in range(a, b+1):
        is_prime = True
        for j in range(2, i):
            if (i % j == 0):
                is_prime = False
        if (is_prime == True):
            ans.append(i)
    return sum(ans)


print(prime_num(a, b))    