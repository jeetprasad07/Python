#creating class
class Student:
    #default constructor
    def __init_subclass__(self):
        pass
    #parameterized constuctor
    def __init__(self,fullname,marks):
        self.name =fullname #obj attribute
        self.marks= marks
    def hello(self):
        print("hello",self.name)

    def get_marks(self):
        print(self.marks)

#creation object

s1 = Student("jeet",89)
s1.hello()
s1.get_marks()
s2 = Student("prasad",90)
s2.hello()
s2.get_marks()
