groups = []
groups.append(list(input().split()))
groups.append(list(input().split()))
groups.append(list(input().split()))

count = [0, 0, 0, 0]

for group in groups:
    # print(group)
    if group[0] == 'Y':
        if int(group[1]) > 37:
            count[0] +=1
        else:
            count[2] +=1
    else:
        if int(group[1]) > 37:
            count[1] +=1
        else:
            count[3] +=1


if count[0]>=2:
    print("E")
else:
    print("N")