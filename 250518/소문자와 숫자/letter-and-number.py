given = input()

for elem in given:
    if (elem.isalpha() == True):
        print(elem.lower(), end="")
    elif (elem.isdigit() == True):
        print(elem, end="")