sent = input()
cnt_ee, cnt_eb = 0, 0

for i in range(len(sent)-1):
    tmp = sent[i:i+2]
    if (tmp == 'ee'):
        cnt_ee += 1
    elif (tmp == 'eb'):
        cnt_eb += 1
    
print(cnt_ee, cnt_eb)