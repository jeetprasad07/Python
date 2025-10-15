class Student:
    def __init__(self,name,marks):
        self.name= name 
        self.marks = marks

    @staticmethod     #decorator
    def college():
        print("RICMS")
s1 = Student("jeet",[99,98,92])
s1.college()