n = int(input())
arr = sorted(list(map(int, input().split())))

print(*arr)
print(*arr[::-1])