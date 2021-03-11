#import cars data
import pandas as pd 
cars=pd.read_csv('cars2.csv',index_col=0)

#convert code to a one-liner,this code below
# dr=cars['drives_right']
# sel=cars[dr]

sel=cars[cars['drivers_right']]

#print sel
print(sel)