num = int(input("ente a natural numbere :"))

fact=1
i=1
while i<=num:
    fact*=i
    print(f"{i}*", end=" ")
    i+=1

print("=",fact)

