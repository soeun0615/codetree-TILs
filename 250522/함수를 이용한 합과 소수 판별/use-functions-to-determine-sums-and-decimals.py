a, b = map(int, input().split())

# Please write your code here.
def find_num(a, b):
    cnt = 0
    for i in range(a, b+1):
        is_prime = True
        for j in range(2, i): # 소수판단
            if (i%j == 0):
                is_prime = False

        if (is_prime == True): # 소수인 경우 자릿수의 합 구하기
            temp = list(str(i))
            sum_t = 0

            for l in range(len(temp)):
                sum_t += int(temp[l])

            if (sum_t % 2 == 0):
                cnt += 1
    return cnt


print(find_num(a, b))    