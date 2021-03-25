#Import cars data
import pandas as pd
cars=pd.read_csv('cars2.csv',index_col=0)

#code for loop that adds COUNTRY column 
for lab, row in cars.iterrows():
    cars.loc[lab,'COUNTRY']=row['country'].upper()
    
#print cars
print(cars)