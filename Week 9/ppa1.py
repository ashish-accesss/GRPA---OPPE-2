'''Write a recursive function named triangular that accepts a positive integer n as
argument and returns the sum of the first n positive integers.

You do not have to accept input from the user or print the output to the console. You just
have to write the function definition.'''
def triangular(n):

    '''Compute the sum of the first n positive integers.

    Parameters:
    n: integer
    Return:
    result: integer'''

    if n == 1:
        return 1
    return n + triangular(n-10)