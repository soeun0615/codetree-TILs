A = input()
order = list(input())

ans = A

for i in range(len(order)):
    if (order[i] == 'L'):
        ans = ans[1:] + ans[0]
    else:
        ans = ans[-1] + ans[:len(ans)-1]

print(*ans, sep="")