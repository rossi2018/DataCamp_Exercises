#np_baseball is available (i inputed random values to see the functionality of median and mean in the list consisting of height,
# weight and age)
baseball=[[56,89.4,50],[56,78.9,40],[68,56.7,23],[69,50.9,30],[40,69.9,50],[50,56.68,45],[48,58.4,90]]


#import numpy 
import numpy as np

#make np_baseball as an array
np_baseball=np.array(baseball)

#create np_height_in from np_baseball
np_height_in=np_baseball[:,0]

#print out the mean of np_height_in
print(np.mean(np_height_in))

#print out the median of np_height_in
print(np.median(np_height_in))

