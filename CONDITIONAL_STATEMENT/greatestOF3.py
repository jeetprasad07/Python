#find the greatest among 3 numbers....

a = int(input("Enter the first no :"))

b = int(input("Enter the second no :"))

c = int(input("Enter the third no :"))

if a > b and a > c :

    print("a is greatest", a)

elif b > a and b > c :

    print("b is greatest", b)

else :
    print("c is greatest", c)