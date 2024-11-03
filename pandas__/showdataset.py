import pandas as safa

datasafa= safa.read_csv( 'BostonHousing.csv' )
safa.options.display.max_rows=506
#print(datasafa.to_string())#to print the entire data
print(datasafa)
#print(safa.options.display.max_rows) 
print(safa.tail()) #last 5 data
print(safa.head()) #first 5 data