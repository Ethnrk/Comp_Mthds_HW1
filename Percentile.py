# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:35:53 2017

@author: Ethan
"""
#test list for checking if code is right
listy = [2,14,67,44,67,34,56,78,12,3,3,98,77,88,43,25,46,76,54,36,73,56,23,87,12,67,34,56,23,98,23,65,33,24,26,97,104,45,67,8,81,98,212]
## lets make this a bit more realistic for diameters shall we??
for i in range(0,len(listy)):
    listy[i] = listy[i]/1000.0

    
##Initialization of code and input of values
print 'Welcome to the river properties calculator!'
print 'You will be given a variety of parameters to enter in.'
print 'For the parameter you wish to solve for, please enter 0 for the value'

r_slope = input('Enter river slope: ')
r_height = input('Enter flow height: ')
## Important!! program does not function with lists of less than three values. As the program is intended to work with longer lists
##(5+ values) this should be ok. If you want to do it with less do the math yourself. It is good mental excercise.
r_diameter = input('Enter a list of grain diameters: ')
sediment_size = {}
sediment_size['set1'] = r_diameter


## defining class for river
class River:
    def __init__(self, slope, height, density , tau):
        self.slope = slope
        self.height = height
        self.density = density
        self.tau = tau
#set up of custom river class
my_river = River (r_slope,r_height,2650.0,0.06)



# preparation for funciton used to caluclate percentile. 

# had issues with getting funciton to accept a direct list, dictionary result was much better
def percentile(data,num):

    Percentile = float(num)
    datum = data['set1'];
    listy1 = sorted(datum)
            
    per_calc = len(listy1)
    a = (Percentile/100.0)
## calculating percentile based on simple statisticla method

    #percentile if list has even number of values
    if per_calc%2 == 0.0:
        count = int(a * per_calc)
        
        x_percentile = (listy1[count] + listy1[count+1])/2.0
    # percentile if it has odd number of values   
    else:
        count = int(a * per_calc) + (a%per_calc >0)
        x_percentile = listy1[count]
        
    return x_percentile

if r_diameter == 0:
    diam_50 = 0
else:
    diam_50 = (percentile(sediment_size,50.0))
    
#set density factor
dens = (1000.0/(my_river.density - 1000))

##solving for variables/ calling you out for doing something you are not supposed to
## uses equation of tau = density difference * height * slope / 50th percentile diameter
if my_river.slope == 0 and my_river.height == 0:
    print("I'm sorry, you appear to be trying to solve for one too many variables, please try again")
    
elif my_river.slope == 0 and r_diameter == 0:
    print("I'm sorry, you appear to be trying to solve for one too many variables, please try again")
    
elif my_river.height == 0 and r_diameter == 0:
    print("I'm sorry, you appear to be trying to solve for one too many variables, please try again")
    
elif my_river.slope ==0:
    slope = (my_river.tau*diam_50)/(dens*my_river.height)
    print 'Slope is:', slope

elif my_river.height == 0:
    height = ((my_river.tau*diam_50)/(dens*my_river.slope))
    print 'Height is: ', height
elif diam_50 == 0:
    diam_50 = (dens*my_river.height*my_river.slope)/my_river.tau
    print '50th percentile diameter is :', diam_50
else:
    print 'Hey man, you already got all the vlaues you need, what are you doing??'









