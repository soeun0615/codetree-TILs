n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.
def sum_interval(_list):
    global arr
    for i in range(len(_list)):
        tmp = arr[_list[i][0]-1 : _list[i][1]]
        sum_val = sum(tmp)
        print(sum_val)


sum_interval(queries)