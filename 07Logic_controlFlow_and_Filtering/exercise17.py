#Import cars data 
import pandas as pd 
import numpy as np
cars=pd.read_csv('cars2.csv',index_col=0)

#Extrac drives_right as series: dr
dr=cars['drivers_right']

#Use dr to subset cars: sel 
sel=cars[dr] # this code try to find all observations in cars where drives_right is True.

#print sel
print(sel)