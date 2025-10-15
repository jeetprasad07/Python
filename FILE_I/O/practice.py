with open("practice.txt","r+") as f:
    f.write("Hi everyone\n")
    f.write("We ar learning File I/O\n")
    f.write("using java\n")
    f.write("I like programming in java.\n")

with open("practice.txt","r+") as f:
    data =f.read()

newdata = data.replace("java","python")
print(newdata)
with open("practice.txt","r+") as f:
    f.write(newdata)