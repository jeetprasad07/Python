f = open("demo.txt","r")

data =f.read()
print(data)
print(type(data))
f.close()

f = open("demo.txt","w")

f.write("I am going to home tomorrow ::::")

f.write("I am going to home  ::::")
f.close()
