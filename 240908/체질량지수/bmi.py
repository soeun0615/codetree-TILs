import math

h, w = map(int, input().split())
b = (10000*w)//(h*h)
b2 = math.floor((10000*w)/(h*h))

print(f'{b}')

if b>=25:
    print("Obesity")