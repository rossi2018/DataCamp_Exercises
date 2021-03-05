#import cars data
import pandas as pd
cars=pd.read_csv('cars2.csv',index_col=0)

#print out drives_right value of Morocco
print(cars.loc['MOR',['drivers_right']])

#print sub-DataFrame 
print(cars.loc[['RU','MOR'],['country','drivers_right']])

