import sys

max_v, min_v = -sys.maxsize, sys.maxsize

for _ in range(3):
    word = input()
    if (len(word) > max_v):
        max_v = len(word)
    if (len(word) < min_v):
        min_v = len(word)

print(max_v - min_v)