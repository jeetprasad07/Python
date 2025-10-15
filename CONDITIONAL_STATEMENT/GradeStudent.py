#grade students based on marks......
    
marks = int(input( "enter the total mark :"))

if 90 <= marks and marks <= 100 :
    print("Grade A")
elif 80 <= marks and marks <= 90 :
    print("Grade B")
elif 70<= marks and marks <= 80 :
    print("Grade C")
elif 60 <= marks and marks <= 70 :
    print("Grade D")
elif 0 <= marks and marks <= 60 :
    print("Grade F")
else :
    print("Invalid Marks !!!")

