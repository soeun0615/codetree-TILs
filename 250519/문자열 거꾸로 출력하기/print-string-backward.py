for _ in range(10):
    tmp = input()
    if (tmp == 'END'):
        break
    else:
        for i in range(1, len(tmp)+1):
            if (i < len(tmp)):
                print(tmp[-i], end="")
            else:
                print(tmp[0], end="")
        print()