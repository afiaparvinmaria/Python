import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
s=[1,2,3,4]
myvar= pd.Series(s)
print(myvar)
myvar = pd.DataFrame(mydataset)

print(myvar)