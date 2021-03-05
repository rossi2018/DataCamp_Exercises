#Import cars data
import pandas as pd 
cars=pd.read_csv('cars2.csv',index_col=0)

#print out drivers_right column as series 
print(cars.loc[:,'drivers_right'])

print(cars.iloc[:,2]) #or use iloc in printing drivers_right column

#print out drivers_right column as Dataframe 
print(cars.loc[:,['drivers_right']])

#print out cars_per_cap and drivers_right as DataFrame 
print(cars.loc[:,['cars_per_cap','drivers_right']])