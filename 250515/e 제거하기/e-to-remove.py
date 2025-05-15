given = input()
ind = given.find('e')
given = given[:ind] + given[ind+1:]
print(given)