import pandas as apm
import matplotlib.pyplot as plotdiagram

result= apm.read_csv( '/content/drive/MyDrive/Colab Notebooks/iris.csv' )

colors = {'setosa': 'red', 'versicolor': 'blue', 'virginica': 'green'}
result['color'] = result['species'].map(colors)

result.plot(kind='scatter', x='sepal_width', y='sepal_length', c=result['color'])
plotdiagram.show()





