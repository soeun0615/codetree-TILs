sent = input()
temp = list(sent)

for i in range(len(sent)):
    a, b = sent[0], sent[1]
    if (temp[i] == b):
        temp[i] = a

print(*temp, sep="")