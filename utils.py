# Functions that allow us to easily create and analyze 
# compartmental models.

def my_list_function(x):
    """This is a sample function that returns a list of numbers from 0 to x."""
    my_list = []
    for i in range(x+1):
        my_list.append(i)
    return my_list