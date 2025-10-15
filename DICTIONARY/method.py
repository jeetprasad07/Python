student ={
    "name": "jeet prasad nayak",
    "subject":{
        "phy":97,
        "chem":92,
        "bio":94
    },
    "rollNo":58
}


print(student)
print(student["name"])
print(student["rollNo"])
print(student["subject"])


print(student.keys())

print(len(student.keys()))

print(student.values())

print(student.items())

print(student.get("name"))
print(student.get("name2"))
#print(student["name1"])////ERROR

student.update({"city":"brahmapur"})
print(student.get("city"))













