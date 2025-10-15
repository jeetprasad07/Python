collection = {1,2,3,3,"hello",3,4,5, "hello","world"}

print(collection)
print(type(collection))
print(len(collection))

collection.add("jeet")
collection.add((1,2,3))
#collection.add([1,2,3,3,34])   // error/////

print(collection)

collection.remove("jeet")
print(collection)

collection1 = {1,2,3,3,"hello",3,4,5, "hello","world"}

collection1.clear()
print(collection1)

collection.pop()
print(collection)

# collection1={}
# print(type(collection1))

# collection2=set()
# print(type(collection2))