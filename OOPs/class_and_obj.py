#creating class
class Student:
    college = "RICMS" #class attribute
   # name ="Jeet Prasad"
   #default constructor
    def __init_subclass__(self):
        pass
    #parameterized constuctor
    def __init__(self,fullname):
        self.name =fullname #obj attribute
        print("adding new student in database")

#creation object

s1 = Student("jeet")
print(s1.name,Student.college)
s2 = Student("prasad")
print(s2.name ,Student.college)# college is the class attribute