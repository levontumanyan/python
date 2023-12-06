# User Management: The application should allow administrators to create, update and delete user accounts for teachers and students.
class Course():
    def __init__(self, name, course_code, faculty) -> None:
        self.name = name
        self.course_code = course_code
        self.faculty = faculty

class Person:
    def __init__(self, name, id):
        self.name = name
        if isinstance(id, int) and len(str(abs(id))) == 8:
            self.id = id
        else:
            raise ValueError("Invalid Id")
        
class Administrator(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.students = []

    def create_student(self, name, id):
        student = Student(name, id)
        self.students.append(student)
        return student

    def delete_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
    
    def get_students(self):
        return self.students

class Student(Person):
    def __init__(self, name, id):
        super().__init__(name, id)
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def __str__(self):
        return f"Name: {self.name}, Student Id: {self.id}, Courses: {self.courses}"

admin = Administrator("Melanie", 12312422)

erikos = admin.create_student("Erik Rusis", 12312312)
erikos.add_course("Physics 1200")
erikos.add_course("Bio 1200")
erikos.add_course("Math 1200")

levonos = admin.create_student( "Levon Tumanyan", 41414141 )
levonos.add_course("Math 4100")
levonos.add_course("Bio 4500")
levonos.add_course("Math 2200")

print(levonos)

tigranos = admin.create_student( "Tigran Tumanyan", 141414141 )

print(admin.get_students())