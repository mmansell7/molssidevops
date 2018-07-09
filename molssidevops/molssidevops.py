"""
Main python file for the molssidevops example
"""

#import statements go here


def mean(num_lst):
    """
    Calculates the mean of a list of numbers
    
    Parameters
    ----------
    num_lst : list
    List of numbers to calculate the average of
    
    
    Returns
    -------
    The average/mean of num_lst
    
    
    Examples
    --------
    >>> mean([1,2,3,4,5])
    3.0
    """
    return sum(num_lst) / len(num_lst)


#    s = 0.0
#
#    for num in num_lst:
#        s = s + num
#
#    m = s/len(num_lst)
#
#    return m
#
#a_lst = [1,2,3,4,5,6,7,8,9,10]
#print('a_lst = ' + str(a_lst))
#mn = mean(a_lst)
#print('mean of a_lst = ' + str(mn))
