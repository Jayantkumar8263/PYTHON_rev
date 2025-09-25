'''Write a Python class named Student with two attributes student_id, student_name. Add a new attribute student_class and display the entire attribute and the values of the class. Now remove the student_name attribute and display the entire attribute with values.'''

class Student : 
    student_name = 'naveen mishra'
    student_id = 101
    def info(self):
        print(f"Name of the student is {self.student_name} and his id is {self.student_id}")
a = Student()
a.student_class = 10
a.info()