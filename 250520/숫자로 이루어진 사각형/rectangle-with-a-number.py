n = int(input())

# Please write your code here.
def print_sq_num(n):
    cnt = 1
    for _ in range(n):
        for _ in range(n):
            if (cnt == 10):
                cnt = 1
            print(cnt, end=" ")
            cnt += 1
        print()

print_sq_num(n)