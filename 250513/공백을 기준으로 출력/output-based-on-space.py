sent1 = input()
sent2 = input()

s = sent1 + sent2

for elem in s:
    if (elem != ' '):
        print(elem, end = "")