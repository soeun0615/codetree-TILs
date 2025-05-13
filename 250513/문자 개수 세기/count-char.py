sent = input()
w = input()
cnt = 0

for elem in sent:
    if (elem == w):
        cnt += 1

print(cnt)