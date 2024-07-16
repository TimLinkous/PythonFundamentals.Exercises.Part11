from enum import Enum
from datetime import date
import uuid

class AliveStatus(Enum):
    Deceased = 0
    Alive = 1

class Person():
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus = AliveStatus.Alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = alive

    def update_first_name(self, new_first_name: str):
        self.first_name = new_first_name

    def update_last_name(self, new_last_name: str):
        self.last_name = new_last_name

    def update_dob(self, new_dob: date):
        self.dob = new_dob

    def update_status(self, new_status: AliveStatus):
        self.alive = new_status

class Instructor(Person):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus = AliveStatus.Alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = f"Instructor_{uuid.uuid4()}"

class Student(Person):
    def __init__(self, first_name: str, last_name: str, dob: date, alive: AliveStatus = AliveStatus.Alive):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = f"Student_{uuid.uuid4()}"

class ZipCodeStudent(Student):
    pass

class HighSchoolStudent(Student):
    pass

class Classroom():
    def __init__(self):
        self.students = []
        self.instructors = []

    def add_instructor(self, instructor: Instructor):
        self.instructors.append(instructor)

    def remove_instructor(self, instructor_id: Instructor):
        self.instructors = [inst for inst in self.instructors if inst.instructor_id != instructor_id]

    def add_student(self, student: Student):
        self.students.append(student)

    def remove_student(self, student_id: Student):
        self.students = [stud for stud in self.students if stud.student_id != student_id]

    def print_instructors(self):
        #for key, value in instructors.items()
        for instructor in self.instructors:
            print(f"{instructor.first_name} {instructor.last_name} - {instructor.instructor_id}")
    
    def print_students(self):
        for student in self.students: 
            print(f"{student.first_name} {student.last_name} - {student.student_id}")
