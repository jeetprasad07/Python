list1 =[1,2,3,2,1]
list2 =[1,2,3,4]

copy_list = list1.copy()
copy_list.reverse()
print(list1)
print(copy_list)
   
if (copy_list == list1):
    print("pallindrome")
else:
    print("Not Pallinfrome")

cop_list = list2.copy()
cop_list.reverse()
print(list2)
print(cop_list)
   
if (cop_list == list):
    print("pallindrome")
else:
    print("Not Pallinfrome")
