given = list(input())
given[1], given[-2] = 'a', 'a'

s = ''.join(given)
print(s)