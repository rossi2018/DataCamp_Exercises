#Import cars data
import pandas as pd 
cars=pd.read_csv('cars2.csv',index_col=0)

#Create car_maniac: observation that have a cars_per_cap over 500
cpc=cars['cars_per_cap']
many_cars=cpc>500
cars_maniac=cars[many_cars] #Used many_cars to subset cars in this line

#Print car_manaic 
print(cars_maniac)