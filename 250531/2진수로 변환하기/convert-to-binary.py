n = int(input())

# Please write your code here.
digits = []

while True:
    if (n < 2):
        digits.append(n)
        break

    digits.append(n%2)
    n //= 2

for num in digits[::-1]:
    print(num, end="") 