class College:
    __students = []
    def register(self):
        self.__students.append(self.name)
    def is_a_student(self):
        return self.name in self.__students


class Student(College):
    def __init__(self, name):
        self.name = name


s1 = Student('debasis')
s2 = Student('soyam')
s1.register()
print(s1.is_a_student())
print(s2.is_a_student())