class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass
    def reset_pass(self):
        print(self.__acc_pass)

acc1 = Account("12345","abcdef")
print(acc1.acc_no)

print(acc1.reset_pass())

class Person:
    __name = "jeet prasad" # private attr

    def __hello(self):  # private mathod
        print("hello person")

    def welcome(self):
        self.__hello()

p1 =Person()
p1.welcome()