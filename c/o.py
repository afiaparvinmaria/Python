'''class safaclass:
    x=5

p1=safaclass()
print(p1.x)'''


#__init__() function

class safa:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(name,age) #__init__ is like a constructor

p1= safa("afia parvin maria",24)
print(p1.name)
print(p1.age)




#__str__() function
class safa:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
         return f"{self.name}({self.age}) bubt"
 
p1= safa("afia parvin maria",24) #creating an object
print(p1)
#output-  afia parvin maria(24) bubt 



#object methods
class safa:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def myfunc(this,ami):
        print("my name is", this.name, ami)

p1= safa("afia parvin maria",24)
p1.myfunc("mariamsafa")
