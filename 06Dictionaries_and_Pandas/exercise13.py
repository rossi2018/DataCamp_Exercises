#import cars data
import pandas as pd 
cars=pd.read_csv('cars2.csv',index_col=0)

#print out observation for Japan
print(cars.loc['JPN'])
print(cars.iloc[2])

#print out observation for Australia and Egypt
print(cars.iloc[[1, 6]])