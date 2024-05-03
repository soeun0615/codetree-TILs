num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
m1, d1, m2, d2 = map(int, input().split())

def get_days(month, day):
    result = 0
    for i in range(1, month):
        result += num_of_days[i]
    result += day

    return result

gap1 = get_days(m1, d1)
gap2 = get_days(m2, d2)
gap = gap2-gap1+1

print(gap)