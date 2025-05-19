arr = list(input().split())

sum_val = 0
for s in arr:
    num = ''
    for elem in s:
        if (elem.isdigit() == True):
            num += elem
        else:
            break
    sum_val += int(num)

print(sum_val)