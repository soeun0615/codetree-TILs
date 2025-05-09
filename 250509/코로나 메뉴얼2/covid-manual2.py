ans = []
cnt_arr = [0] * 4

for i in range(3):
    a, b = input().split()
    if (a == 'Y') & (int(b) >= 37):
        ans.append('A')
        cnt_arr[0] += 1
    elif (a == 'N') & (int(b) >= 37):
        ans.append('B')
        cnt_arr[1] += 1
    elif (a == 'Y') & (int(b) < 37):
        ans.append('C')
        cnt_arr[2] += 1
    else:
        ans.append('D')
        cnt_arr[3] += 1

if (cnt_arr[0] >= 2):
    cnt_arr.append('E')

print(*cnt_arr)