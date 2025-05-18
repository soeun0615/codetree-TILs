given = input()

gap = ord('a') - ord('A')
for elem in given:
    if (ord(elem) > ord('a')) & (ord(elem) < ord('z')):
        print(chr(ord(elem) - gap), end="")
    else:
        print(chr(ord(elem) + gap), end="")