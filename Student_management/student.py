class Student():
    def __init__(self, student_id, name, age, course):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.course= course
    def display_student(self):
        print(f'ID: {self.student_id}')
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Course: {self.course}')