#import pandas as pd
import pandas as pd



# Fix import by including index_col
cars = pd.read_csv('cars.csv',index_col=0)


# print out cars
print(cars)
