'''Define a Python function student(). Using function attributes display the names of all arguments.'''
class student_info:
    name = 'P Jayant Kumar'
    standard = '10'
    age = '13'
    def info(self):
        print(f"{self.name} is in {self.standard}")
a = student_info()
#a.name = 'gautam dutta'
#a.standard = 11
a.info()
'''self is a method, argument which we give to the function, which is used to derive it inside a class.'''
#print(a.name, a.standard, a.age)