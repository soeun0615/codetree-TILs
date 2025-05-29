n = int(input())

# Please write your code here.
class Person:
    def __init__(self, name, addr, city):
        self.name = name
        self.addr = addr
        self.city = city

people = []
people_name = []
for _ in range(n):
    name, addr, city = input().split()
    people_name.append(name)
    people.append(Person(name, addr, city))

people_name.sort()
# print(people_name)

for i in range(n):
    if (people[i].name == people_name[-1]):
        ind = i

print(f"name {people[ind].name}")
print(f"addr {people[ind].addr}")
print(f"city {people[ind].city}")