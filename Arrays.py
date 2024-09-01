students= ["sakib","safa","zarin","reem"]
#students[2]="mariam"

print(students[0])
print(students[2])
print("length is " , len(students) , "\n") 
for x in students:
    print(x)
print("\n")    

#adding array elements
students.append("afia")
for x in students:
    print(x)
print("\n") 

#remove elements from array
students.pop(1)
for x in students:
    print(x)
print("\n")

students.remove("sakib")
for x in students:
    print(x)
print("\n")    