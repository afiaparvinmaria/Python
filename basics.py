'''# import sys
# print(sys.version)


#creating variable by assigning values
x=0 #integer
y="i am safa" #string
e,f,g=1,4.5,"bubt" #creating multiple variables in one line
print(x , y)
print(e,f,g)


#intendation of block
if 5>2:
    print("intendation")

if 6>0:
          print("intendation2")


#casting ( if we want to specify the data type)
my=6.8
a= str('safa') # it also can be declared with double quotes "safa"
b= int(my)
c= float(5.6)
print(a,b,c,my)
#we can print the data type of a variable by using type function()
d=type(b)
print(d) #<class 'int'>



#list
a,b=2,3
animals = ["python ",'is ',"joss"]
x,y,z = "animals","water","food"
print(x,y,z)
print(x + y +z)
print(a+b)
p,q,s=animals
print(p+q+s)
print(a,b,animals)
'''

'''
#global variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()
print("Python is " + x)
#OUTPUT:
#Python is fantastic
#Python is awesome

def myfunction():
    global a #i can use this global variable anywhere i want
    a=1
myfunction()

print(a)
'''
'''
#data types
a= "hello" #str
b=30 #int
c=20.4 #float
d=3+6j #complex
e= ["apple", "banana", "cherry"] #list
f= ("apple", "banana", "cherry") #tuple
g= range(6) #range
h= {"name" : "John", "age" : 36} #dict
i={"apple", "banana", "cherry"} #set
j= frozenset({"apple", "banana", "cherry"}) #forzenset
k= True #bool
l=b"hello"#bytes
m= bytearray(5)#bytearray
n=memoryview(bytes(5))
o=None
'''

#random number
import random
print(random.randrange(1, 10)) #generates random numbers

'''#python strings
a="hello"
b='hello'
#multiline strings
c="""i am a student 
my name is safa"""
print(c[0])
#looping a string
for x in c:
    print(x)
#string len
print(len(a))
'''

'''
#if else
a=78
b=98
if a<b :
    print("a is smaller than b")
elif a>b :
    print("a is larger than b")
else :
    print("none")


print("hello") if a>b else print("world")

if not a>b :
    print("a is not greater than b")
if a>b or b>a:
    print("success")
if a > b and b > a:
   print("and success")
   
print("A") if a > b 
    else 
    print("=") if a == b 
        else
        print("B")
        '''

#dictionaries
mydictionaries={
    "A":"mariam",
    9:90,
    "year":2010,
    20:"safa"
}
