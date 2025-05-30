n = 5

class Person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

people = []
for _ in range(n):
    name, height, weight = input().split()
    height, weight = int(height), float(weight)
    people.append(Person(name, height, weight))

# 이름순정렬
people.sort(key = lambda x:x.name)
print('name')
for p in people:
    print(p.name, p.height, p.weight)

print()

#키 순 정렬
people.sort(key = lambda x:-x.height)
print('height')
for p in people:
    print(p.name, p.height, p.weight)