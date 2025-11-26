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

class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()
        self.count = 0

    def add_student(self, student):
            if self.count == 10:
                raise ValueError('Group cannot be more than 10 students.')

            self.group.add(student)
            self.count +=1

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

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 31, 'Steve', 'Jobs', 'AN143')
st4 = Student('Female', 23, 'Liza', 'Taylor', 'AN146')
st5 = Student('Male', 34, 'Steve', 'Jobs', 'AN148')

gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.count = 9
gr.add_student(st3)
gr.add_student(st4)





