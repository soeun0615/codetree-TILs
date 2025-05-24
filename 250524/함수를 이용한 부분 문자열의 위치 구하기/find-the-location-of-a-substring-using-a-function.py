text = input()
pattern = input()

# Please write your code here.
def find_ind():
    if (pattern in text):
        ind = text.index(pattern)
    else:
        ind = -1
    return ind


ans = find_ind()
print(ans)