given = input()
L = len(given)

print(given)
for i in range(L):
    print(given[-(i+1):] + given[:L-(i+1)])