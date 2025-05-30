n = int(input())

class Person:
    def __init__(self, name, height, weight):
        self.name, self.height, self.weight = name, height, weight

people = []
for _ in range(n):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    people.append(Person(name, height, weight))

people.sort(key = lambda x:(x.height, -x.weight))

for p in people:
    print(p.name, p.height, p.weight)