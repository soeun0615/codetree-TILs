attend = {1:'John', 2:'Tom', 3:'Paul', 4:'Sam'}

while True:
    n = int(input())
    if (n in list(attend.keys())):
        print(attend[n])
    else:
        print('Vacancy')
        break