class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'{self.first_name} {self.last_name} is {self.age} years old'

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name} is {self.age} years old. Record book: {self.record_book}'

class TooManyStudentsError(Exception):
    pass

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) == 10:
            raise TooManyStudentsError("Group cannot have more than 10 students.")
        self.group.add(student)

    def delete_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                self.group.remove(student)
                break

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n{all_students} '

gr = Group('PD1')

try:
    for i in range(11):
        gr.add_student(Student("M", 20+int(i), f"Name{i}", f"Surname{i}", f"AN14{i}"))
except TooManyStudentsError as e:
    print(f'Error: {e}')
print(gr)




