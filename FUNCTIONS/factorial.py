def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    print(f"Factorial of {n} = ",fact)


num =int(input("Entr a number :"))
factorial(num)