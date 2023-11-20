# User Management: The application should allow administrators to create, update and delete user accounts for teachers and students.

# class Student:
#     def __init__(self, name, id, courses=[]):
#         self.name = name
#         self.id = id
#         self.courses = courses

#     def add_course(self, course):
#         self.courses.append(course)

#     def remove_course(self, course):
#         self.courses.remove(course)

#     def display_student_info(self):
#         print("Name: ", self.name)
#         print("Student Id: ", self.id)
#         print("Courses: ", self.courses)
        
class Student:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        self.courses.remove(course)

    def display_student_info(self):
        print("Name: ", self.name)
        print("Student Id: ", self.id)
        print("Courses: ", self.courses)



erikos = Student( "Erik Rusis", 12312312 )

erikos.add_course("Physics 1200")

erikos.add_course("Bio 1200")
erikos.add_course("Math 1200")

erikos.display_student_info()



levonos = Student( "Levon Tumanyan", 41414141 )


levonos.add_course("Math 4100")

levonos.add_course("Bio 4500")
levonos.add_course("Math 2200")

levonos.display_student_info()



