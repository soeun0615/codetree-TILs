n = int(input())

ans = input().split()
word = ""
for w in ans:
    word += w

for i in range(len(word)//5):
    print(word[i*5:(i+1)*5])
if (len(word)%5 > 0):
    print(word[-(len(word)%5)::])