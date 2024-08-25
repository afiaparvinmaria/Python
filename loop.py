'''i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")'''


#FOR LOOP
'''student=["safa","sakib",48,509]
for x in student:
    print(x,end=' ')#end is used for not having a new line by default

for x in "mariam safa": #iterrating each character of the string
     print(x,end='')

fruits=["apple","pitaya","bannana","cherry"]
 
for x in fruits:
   if x=="bannana":
       break
   if x=="pitaya":
       continue
   print(x) '''

for x in range(6):
    print(x)  #prints 0 to 5     
for x in range(2,9): #prints 2 to 9
    print(x)
for x in range (2,20,2):
    print(x)
else:
    print("all finished")    


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass #used for an empty for loop    
