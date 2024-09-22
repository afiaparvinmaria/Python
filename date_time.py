import datetime

x = datetime.datetime.now()
print(x)  #2024-09-08 17:11:42.484610
print (x.year) #2024
print(x.strftime("%A"))#sunday


#creating date objects using datetime() class(constructor)
#it requires three parameters to create a daye: year, month, day
y= datetime.datetime(2020,5,26)# #2024-09-08 00:00:00
print(y)


#strftime()
z= datetime.datetime(2018, 6, 1) #June
print(z.strftime("%B"))#prints month
print(z.strftime("%z"))#timezone


