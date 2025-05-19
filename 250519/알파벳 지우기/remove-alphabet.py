sum_val = 0

for _ in range(2):
    s = input()
    num = ''
    for elem in s:
        if (elem.isdigit() == True):
            num += elem
    sum_val += int(num)
print(sum_val)