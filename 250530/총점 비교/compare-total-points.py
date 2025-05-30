n = int(input())

class Student:
    def __init__(self, name, s1, s2, s3):
        self.name, self.s1, self.s2, self.s3 = name, s1, s2, s3

students = []
for _ in range(n):
    name, s1, s2, s3 = input().split()
    s1, s2, s3 = int(s1), int(s2), int(s3)
    students.append(Student(name, s1, s2, s3))

students.sort(key = lambda x:(x.s1 + x.s2 + x.s3))

for s in students:
    print(s.name, s.s1, s.s2, s.s3)