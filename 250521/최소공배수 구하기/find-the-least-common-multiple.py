n, m = map(int, input().split())

# Please write your code here.
def find_lcm(n, m):
    n_list = [n * i for i in range(1, m+1)]
    m_list = [m * i for i in range(1, n+1)]

    for elem in n_list:
        if (elem in m_list):
            print(elem)
            break


find_lcm(n, m)    