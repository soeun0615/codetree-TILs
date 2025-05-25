n = int(input())

# Please write your code here.
def print_sent(n):
    if (n==0):
        return
    print_sent(n-1)
    print("HelloWorld")


print_sent(n)    