def my_func(name):
    print("hello ami" + name )

my_func("safa")


#arbitary arguments *args
#if i dont know how many arguments will be passed into the function, add a * before the parameter

def my_func2(*names):
    print(names[2],names[0])

my_func2("mariam","safa","mim","arnob") #prints mim mariam


#keyword arguments 
def my_func3(b,a,c):
    print(c)
    print(b)
    print(a)

my_func3(a=6,c=7,b=1)


#arbitary keywork arguments **Kwargs
#if i dont know how many keyword arguments will be pass, use ** before the parameter
def my_func4(**a):
    print(a["a"])

my_func4(a="2",b="3")


#positional arguments/normal arguments

#Default Parameter Value
#Passing a List as an Argument
#Return Values
#The pass Statement

#Positional-Only Arguments
#Keyword-Only Arguments
#Combine Positional-Only and Keyword-Only

