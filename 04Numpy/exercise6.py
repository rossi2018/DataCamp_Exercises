#Create basball, a list of lists
baseball=[[180,78.4],[215,102.7],[210,98.5],[188,75.2]]

#import numpy
import numpy as np

#create a 2d numpy array from baseball: np_baseball
np_baseball=np.array(baseball)

#print out the type of np_bseball
print(type(np_baseball))

#print out the shape of np_baseball
print(np_baseball.shape)