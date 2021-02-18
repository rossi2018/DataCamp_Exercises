#np_baseball is available (i inputed random values to see the functionality of median and mean in the list consisting of height,
# weight and age)
baseball=[[56,89.4,50],[56,78.9,40],[68,56.7,23],[69,50.9,30],[40,69.9,50],[50,56.68,45],[48,58.4,90]]

#import numpy
import numpy as np

#make np_baseball as an array 
np_baseball=np.array(baseball)

#print mean height (first column)
avg=np.mean(np_baseball[:,0])
print("Average:" + str(avg))

#print median height. 
med=np.median(np_baseball[:,0])
print("Median:" + str(med))

#print out the standard deviation on height 
stddev=np.std(np_baseball[:,0])
print("Standard deviation:"+ str(stddev))

#print out correlation between first and second column
corr=np.corrcoef(np_baseball[:,0])
print("correlation: " + str(corr)) 