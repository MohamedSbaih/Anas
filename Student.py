import random

# data = [{"name":"Anas",
#          "id":123,
#          "class":"B"
#          },
#
#         {"name": "Mohamed",
#          "id": 333,
#          "class": "C"
#          }
#
#         ]
allStudent = [{

}]



class Student:
    def __int__(self, name, id, student_class, courses):
        self.name = name
        self.id = id
        self.student_class = student_class
        self.courses = courses



        # Return True if condition True
    def checkCourse(self, course_class):
        allStudents = ["A", "B", "C"]
        return course_class in allStudents

    def format_data(self,student_name,id,student_class):
        """Takes the student data and returns the printable format."""
        for i in allStudent:
            case = {'name': student_name, 'class':student_class, 'id':id }
            allStudent.append(case)


    def addCourse(self):

        studentName = input("Enter Student Name: ")
        studentClass = input("Enter Student Class (A-B-C): ")
        studentId = input("Enter Student Id")
        if self.checkCourse(studentClass):
            self.format_data(studentName,studentClass,studentId)
            print("Student Saved Successfully")
        else:
            print("Select Class Again")


    def check_user(self, id,data):
       return id in data


    def index(self):
        for i in range(len(allStudent)):
            if (id in allStudent[i]):
                allStudent.remove(allStudent[i])
                return i

    def remove_student(self,i):
        id = input("Enter Student ID")
        #data is list for all details
        if self.check_user(id,allStudent):
            allStudent.remove(allStudent[i])
            print("Delete Done Successful")
        else:
            print("User Not Exist")


    def edit_students(self):
        user = input("Enter Student Id")
        if self.check_user():
            newName = input("enter new name")
            newClass = input("enter new class")
            newId = input("enter new id")
            i = self.index()
            self.format_data(newName,newClass,newId)
            allStudent.append(allStudent[i])

        else:
            print("user not exist")

    def student_details(self):
        """Prints the all Details"""
        print(f"Name: {self.name}")
        print(f"Student id: {self.id}")
        print(f"Student class: {self.student_class}")
        print(f"Student courses: {self.courses}")


    def course_student(self):
        id = int(input("Enter format_data"))
        for i in range(len(allStudent)):
            if(id in allStudent[i]):
               if(self.check_user(id, allStudent)):
                   self.addCourse()
               else:
                   print("course not exist")


