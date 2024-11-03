'''import pandas as safa


#series
a=[1,2,4]
#myseries= safa.Series(a)
myseries= safa.Series(a, index=["one","two","three"]) #naming the labels
print(myseries)
print(myseries[0])
print(myseries["one"])#labels


#Key/Value Objects as Series
calories= {"one":20,"two":30,"three":40}
print(safa.Series(calories, index=["one","two"]))#Create a Series using only data from "one" and "two"



#dataframes
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

#myvar = safa.DataFrame(mydataset)
myvar= safa.DataFrame(mydataset,index=["one","two","three"])

#print(myvar)
#print(myvar.loc[0])#BMW 3
print(myvar.loc[["one","two","three"]])#BMW 3, Volvo 7, Ford 2'''
import pandas as safa

datasafa= safa.read_csv( 'BostonHousing.csv' )
print(datasafa)



