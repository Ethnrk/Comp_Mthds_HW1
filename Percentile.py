# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 16:35:53 2017

@author: Ethan
"""
Percentile = float(50)
listy = [2,14,67,44,67,34,56,78,12,3,3,98,77,88,43,25,46,76,54,36,73,56,23,87,12,67,34,56,23,98,23,65,33,24,26,97,104,45,67,8,81,98,212]
listy1 = sorted(listy)
        
per_calc = len(listy1)
a = (Percentile/100)

if per_calc%2 == 0:
    count = int(a * per_calc)
    x_percentile = (listy1[count] +listy1[count+1])/2
   
else:
    count = int(a * per_calc) + (a%per_calc >0)
    x_percentile = listy1[count]
    
print x_percentile