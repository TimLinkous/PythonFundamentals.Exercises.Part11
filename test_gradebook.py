import unittest
from gradebook import Person, Instructor, Student, ZipCodeStudent, HighSchoolStudent, Classroom, AliveStatus
from datetime import date

class TestGradeBook(unittest.TestCase):

    def setUp(self):
        self.classroom = Classroom()
        self.instructor1 = Instructor("Tim", "Linkous", date(1992, 9, 9))
        self.instructor2 = Instructor("John", "Doe", date(2001, 1, 1))
        self.student1 = ZipCodeStudent("Codey", "McCoderson", date(1980, 7, 15))
        self.student2 = HighSchoolStudent("Jane", "Smith", date(1996, 9, 25))

    def test_add_instructor(self):
        self.classroom.add_instructor(self.instructor1)
        self.assertEqual(len(self.classroom.instructors), 1)
        self.classroom.add_instructor(self.instructor2)
        self.assertEqual(len(self.classroom.instructors), 2)

    def test_add_student(self):
        self.classroom.add_student(self.student1)
        self.assertEqual(len(self.classroom.students), 1)
        self.classroom.add_student(self.student2)
        self.assertEqual(len(self.classroom.students), 2)

    def test_remove_instructor(self):
        self.classroom.add_instructor(self.instructor1) #calls the add_instructor method of the Classroom instance self.classroom
        self.classroom.add_instructor(self.instructor2) #adds instructors 1 and 2 to to the list of instructors in the classroom
        self.classroom.remove_instructor(self.instructor1.instructor_id) #calls remove_constructor method of the Classroom instance self.classroom
        self.assertEqual(len(self.classroom.instructors), 1) #asserts that the length of the instructors list in self.classroom is 1. Checks if the instructor was successfully removed, leaving only one instructor in the list.
        self.assertEqual(self.classroom.instructors[0].instructor_id, self.instructor2.instructor_id)

    def test_remove_student(self):
        self.classroom.add_student(self.student1)
        self.classroom.add_student(self.student2)
        self.classroom.remove_student(self.student1.student_id)
        self.assertEqual(len(self.classroom.students), 1)