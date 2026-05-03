'''Write a recursive function named multiply accepts two positive integers a and b as
argument and returns their product. You can only use + and - operators. You are not
allowed to use the * symbol anywhere in your code!

You do not have to accept input from the user or print the output to the console. You just
have to write the function definition.'''
def multiply(a, b):
    '''
    A recursive function to compute the product of two numbers

    Parameters:
    a, b: integers
    Return:
    result: integer'''

    if b == 0:
        return 0
    if b<0:
        return -multiply(a,-b)
    return a+multiply(a,b-1)