'''The factorial of a positive integer n is defined as follows:

n != 1.2. 3 ... n
Write a recursive function named factorial that accepts a positive integer n as
argument and returns the factorial of n.

You do not have to accept input from the user or print the output to the console. You just
have to write the function definition.'''
def factorial(n):

    '''Compute the factorial of n.

    Parameters:
    n: integer
    Return:
    result: integer
    '''
    if n == 1 or n == 0:
        return 1
    return n*factorial(n-1)