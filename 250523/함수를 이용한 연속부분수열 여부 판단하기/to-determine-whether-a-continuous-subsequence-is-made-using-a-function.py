n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def find_list(a, b):
    ans = 'No'
    for i in range(n1 - n2 + 1):
        temp = a[i:i+n2]
        # print(temp)
        if (temp == b):
            ans = 'Yes'
    print(ans)


find_list(a, b)