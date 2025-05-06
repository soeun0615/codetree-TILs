for i in range(19):
    for j in range(19):
        if (j%2==1)|(j==18):
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end="\n")
        elif (j%2==0):
            print(f"{i+1} * {j+1} = {(i+1)*(j+1)}", end=" / ")