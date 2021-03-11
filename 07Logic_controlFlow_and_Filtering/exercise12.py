z=6
if z%2==0:
    print('z is divisible by 2') # True

elif z % 3 ==0:
    print('z is divisible by 3') # Never reached 

else:
    print('z is neither divisible by 2 nor by 3')


#Both the if and elif conditions hold in this case.Will two printouts occur? Nope.
#As soon as python bumps into a condition that it's true, it executes the corresponding
#code and then leaves the control structure after that.This means the second condition, 
# corresponding to the elife, is never reached so there's no corresponding printout  