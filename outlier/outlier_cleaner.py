#!/usr/bin/python
import math

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    #cleaned_data = []
    temp = []
    #print len(predictions)
    ### your code goes here
    for num in range(0,len(predictions)):
        error = abs(predictions[num] - net_worths[num])
        temp.append([ages[num],net_worths[num],error])
    temp = sorted(temp, key=lambda x: (x[2]))
    #print temp,len(temp)
    cuted_num = 0 - int(math.ceil(len(temp)/10))
    #print cuted_num
    cleaned_data = temp[:cuted_num]
    #print cleaned_data,len(cleaned_data)
    #print len(cleaned_data)
    return cleaned_data

