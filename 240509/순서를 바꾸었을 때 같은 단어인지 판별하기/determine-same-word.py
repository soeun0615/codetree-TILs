A = input()
arr_A = list(A)
arr_A.sort()

B = input()
arr_B = list(B)
arr_B.sort()

#순서를 바꿔서 동일한 단어로 만들려면
# 1. 문자의 전체 수가 같아야하고
# 2, 문자 종류와 수가 같아야함

if len(arr_A) == len(arr_B):
    for i in range(len(A)):
        #print("i = ", i)
        if arr_A[i] == arr_B[i]:
            result = 0
            pass
        else:
            result = 1
            break

    if result == 0:
        print("Yes")
    else:
        print("No")

else:
    print("No")