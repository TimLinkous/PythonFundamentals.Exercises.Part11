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