#Import cars data
import pandas as pd
cars=pd.read_csv('cars2.csv',index_col=0)

#Use .apply(str.upper)

#for lab, row in cars.iterrows():
#   cars.loc[lab,'COUNTRY']=row['country'].upper()

#print(cars) # It work but use the below alternatives which make use of a single line

cars['COUNTRY']=cars['country'].apply(str.upper)

print(cars)