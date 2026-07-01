from student import Student
from validators import integer_validator, string_validator
class StudentManagement():
    def __init__(self):
        self.students = [ ]
    def add_student(self):
        student_id = integer_validator('Enter student ID number: ', 1, 1000)
        for student in self.students:
            if student.student_id == student_id:
                print('Student ID already exists')
                return
        name = string_validator('Enter student name: ')
        age = integer_validator('Students age: ', 18,40)
        course = string_validator('Enter course: ')
        student = Student(student_id, name, age, course)
        self.students.append(student)
        print(f'{name} details added successfully')
    def view_student(self):
        for item in self.students:
            item.display_student() 
    def search_student(self):
        search_id = integer_validator('Enter student ID: ',1,1000)
        found = False
        for student in self.students:
            if search_id == student.student_id:
                student.display_student()
                found = True
                break
        if found == False:
            print('Student not found')
    def update_student(self):
        update_id = integer_validator('Enter student ID: ',1,1000)
        found = False
        for student in self.students:
            if update_id == student.student_id:
                student.student_id = integer_validator('Enter a new ID to update: ', 1,1000)
                student.name = string_validator('Enter a new name: ')
                student.age = integer_validator('Enter a new age: ')
                student.course = string_validator('Enter a new course: ')
                found = True
                print('Suceesfully updated student info')
                student.display_student()
                break
        if found == False:
            print('Student not found') 
    def delete_student(self):
        delete_id = integer_validator('Enter students ID you wish to delete: ',1,1000)
        found = False
        for student in self.students:
            if delete_id == student.student_id:
                student.display_student()
                self.students.remove(student)
                found = True
                print('Student successfully deleted')
                break
        if found == False: 
            print('Student not found')
    def menu(self):
        print('Welcome to Student Portal')
        while True:
            print('1. add_student')
            print('2. view_student')
            print('3. search_student')
            print('4. update_student')
            print('5. delete_student')
            print('6. Exit')
            choice = integer_validator('What do you want to do: ',1,6)
            if choice == 1:
                self.add_student()
            elif choice == 2:
                self.view_student()
            elif choice == 3:
                self.search_student()
            elif choice == 4:
                self.update_student()
            elif choice == 5:
                self.delete_student()
            elif choice == 6:
                print('Goodbye')  
                break
            else:
                print('Invalid choice, Try again')