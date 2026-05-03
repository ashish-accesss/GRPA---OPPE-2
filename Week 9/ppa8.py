'''Write a recursive function named non_decreasing that accepts a non-empty list L of integers as argument
and returns True if the elements are sorted in non-decreasing order from left to right, and False otherwise.

You do not have to accept input from the user or print the output to the console. You just have to write the
function definition.'''
def non_decreasing(L):

    '''A recursive function that determines if L is sorted in non-decreasing order.

Parameters:
L: list of integers
Return:
result: bool'''

    if len(L) <= 1:
        return True
    if L[0]>L[1]:
        return False
    return non_decreasing(L[1:])