import  Course
import Student
from Student import Student

student = Student()
course = Course()

userSelect = int(input("""Select Choice Please
1- Add New Student
2- Remove Student
3- Edit Student 
4- Display All Student
5- Greate New Course
6- Add Course to stdent
0- Exit
"""))

is_true = True

while is_true:
    match userSelect:
        case 1:
            student.addCourse()
        case 2:
            student.remove_student()
        case 3:
            student.edit_students()
        case 4:
            student.student_details()
        case 5:
            student.addCourse()
        case 6:
            student.course_student()
        case 0:
            is_true = False
        case other :
            print("Try again")

