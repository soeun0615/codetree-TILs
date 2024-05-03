hours1, mins1, hours2, mins2 = map(int, input().split())

gap = (hours2*60 + mins2*1) - (hours1*60 + mins1*1)

print(gap)