n = int(input())

class Student:
    def __init__ (self, name, kor, eng, math):
        self.name, self.kor, self.eng, self.math = name, kor, eng, math

students = []
for _ in range(n):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(Student(name, kor, eng, math))

students.sort(key = lambda x:(-x.kor, -x.eng, -x.math))

for s in students:
    print(s.name, s.kor, s.eng, s.math)