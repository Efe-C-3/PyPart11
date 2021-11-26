from enum import Enum
from uuid import uuid4


class AliveStatus(Enum):
    deceased = 0
    alive = 1


class Person:

    def __init__(self, first_name, last_name, dob, alive):
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob
        self.alive = AliveStatus.alive

    def update_first_name(self):
        return self.first_name

    def update_last_name(self):
        return self.last_name

    def update_dob(self):
        return self.dob

    def update_status(self):
        self.alive = AliveStatus.deceased if self.alive == AliveStatus.alive else AliveStatus.alive




class Instructor(Person):
    def __init__(self, instructor_id, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = 'Instructor_{}.format(uuid4())'



class Student(Person):

    def __init__(self, student_id, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = 'Student_{}.format(uuid4())'


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)

class CollegeStudent(Student):
    def __init__(self, first_name, last_name, dob):
        super().__init__(first_name, last_name, dob)


class Classroom:
    def __init__(self):
        self.students = {}
        self.instructors = {}

    def add_instructor(self, instructor):
        if instructor.instructor_id not in self.instructors:
            self.instructors[instructor.instructor_id] = instructor
        return self.instructors

    def remove_instructor(self, instructor_id):
        if instructor_id in self.instructors:
            del self.instructors[instructor_id]
        return self.instructors

    def add_student(self, student):
        if student.student_id not in self.students:
            self.students[student.student_id] = student
        return self.students

    def remove_student(self, student_id):
        if student_id in self.students:
            del self.students[student_id]
        return self.students

    def print_instructors(self):
        for instructor in self.instructors.values():
            print('{} {} {} {} {}.format(instructor.instructor_id, instructor.first_name, instructor.last_name, instructor.dob, instructor.alive')

    def print_students(self):
        for student in self.students.values():
            print('{} {} {} {} {}.format(student.student_id, student.first_name, student.last_name, student.dob, student.alive')
