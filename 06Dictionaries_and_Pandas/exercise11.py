#import cars data
import pandas as pd
cars=pd.read_csv('cars2.csv',index_col=0)

#print out country column as pandas series
print(cars['country']) 

#print out country column as pandas DataFrame
print(cars[['country']])

#print out DataFrame with country amd drives_right colums
print(cars[['country','drivers_right']])