marks =[78,48,89,50,78]
marks[1:4] # is 78,48,50 last index is not include
marks[:4]#is the same as marks[0:4]
marks[1:]#is same as marls[1:len(marls)]
marks[-3:-1] is [33,95]

print(marks[1:4])
print(marks[:4])
print(marks[1:])
print(marks[-3:-1])

marks.append(89)
marks.sort()
print(marks[:6])
marks.sort(reverse=True)
print(marks[:6])
marks.reverse()
print(marks[:6])
marks.insert(3,67)
print(marks[:6])

