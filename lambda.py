#A lambda function is a small anonymous function.
#A lambda function can take any number of arguments, but can only have one expression.
x = lambda a : a + 10 #syntax- lambda arguments : expression
print(x(5))

x=lambda a,b: a-b
print(x(10,6))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2) #mydoubler is a lambda function when the myfunc returns the lambda

print(mydoubler(11))