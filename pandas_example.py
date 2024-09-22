import pandas as safa



mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = safa.DataFrame(mydataset)

print(myvar)