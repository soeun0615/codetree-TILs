input_str, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

ans = input_str
# Please write your code here.
for i in range(len(queries)):
    if (queries[i] == 1):
        ans = ans[1:] + ans[0]
    elif (queries[i] == 2):
        ans = ans[-1] + ans[:len(ans)-1]
    else:
        temp = list(ans)
        for i in range(len(ans)//2):
            temp[i], temp[len(ans)-i-1] = ans[len(ans)-i-1], ans[i]
        ans = ''.join(temp)
    print(ans)