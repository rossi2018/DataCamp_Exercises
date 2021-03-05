#import cars data
import pandas as pd 
cars=pd.read_csv('cars2.csv',index_col=0)

#print out first 3 observaion
print(cars[0:3])

#print out fourth,fifth and sixth observation 
print(cars[3:6])
