import pandas as safa
#cleaning empty cells
result= safa.read_csv('BostonHousing.csv')
finalresult= result.dropna() #remove all empty cells rows and retruns a clean dataframe
#the dropna() method returns a new DataFrame, and will not change the original.
#print(finalresult.to_string())


# to change the original file
result.dropna(inplace= True)
print(result.to_string())


#replace empty cells with new values
result.fillna(130, inplace = True) #fills all the empty cells with 130 value