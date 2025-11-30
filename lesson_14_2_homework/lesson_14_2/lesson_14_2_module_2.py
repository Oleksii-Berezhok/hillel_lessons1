from lesson_14_2_module_1 import Human

class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'Student: {self.first_name} {self.last_name} is {self.age} years old. Record book: {self.record_book}'

    def __eq__(self, other):
        if isinstance(other, Student):
            return str(self) == str(other)

        return False

    def __hash__(self):
        return hash(str(self))