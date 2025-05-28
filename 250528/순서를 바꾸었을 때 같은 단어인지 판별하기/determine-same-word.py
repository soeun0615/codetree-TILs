word1 = input()
word2 = input()

# Please write your code here.
list_1 = list(word1)
list_2 = list(word2)
list_1.sort()
list_2.sort()

if (list_1 == list_2):
    print("Yes")
else:
    print("No")