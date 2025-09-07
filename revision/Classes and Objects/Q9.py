'''Write a Python class named Student with two attributes student_name, marks. Modify the attribute values of the said class and print the original and modified values of the said attributesz'''

from Q10 import Student


class student :
    student_name = 'Harsha tiwari'
    Class = '12th'
    age = 16
    print(f"name of the student is {student_name} and his age is {age} ")
    setattr(Student, 'student_name', 'Angel Brooks')
    setattr(Student, 'marks', 95) 
    print(f"Student Name: {getattr(Student, 'student_name')}")
student()