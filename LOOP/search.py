#suqares

muns =(1,4,9,16,25,36,49,64,81,100)

#Travese
i =0
x= len(muns)-1
while i<=x:

    print(f"element at index {i}={muns[i]}")
    i+=1

y =int(input("Enter a number you want to search : "))

a= 0
found =False
while a<=len(muns)-1:
    if(muns[a]== y):
        print(f"FOUND AT INDEX {a}={muns[a]}")
        found=True
        break #exit the loop

a+=1

if not found:
    print("Number not found in the list .")