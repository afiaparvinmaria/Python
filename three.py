import pandas as apm

result= apm.read_csv( '/content/drive/MyDrive/Colab Notebooks/iris.csv' )

print(result.corr(numeric_only= True))





