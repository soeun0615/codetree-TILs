n = int(input())

class Person:
    def __init__(self, name, h, w):
        self.name, self.h, self.w = name, h, w

people = []
for _ in range(n):
    name, h, w = input().split()
    person = Person(name, h, w)
    people.append(person)

people.sort(key = lambda x:x.h)

for p in people:
    print(p.name, p.h, p.w)