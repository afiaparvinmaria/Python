#1st part
import pandas as apm

result= apm.read_csv( '/content/drive/MyDrive/Colab Notebooks/iris.csv' )
result.dropna(inplace= True)
print(result.to_string())



#2nd part
import pandas as apm

result= apm.read_csv( '/content/drive/MyDrive/Colab Notebooks/iris.csv' )
result.dropna(inplace= True)
result['species']=result['species'].str.replace(' ', '')
print(result.to_string())


