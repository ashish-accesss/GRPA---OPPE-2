'''A polynomial is a mathematical function of the following form:

f(x) = a0*x^0 + a1*x^1 + a2*x^2 + ... + an*x^n

The ai's are called the coefficients of the polynomial and uniquely determine it.
This polynomial can be represented in Python using a list of its coefficients:

L = [a0, a1, a2, ..., an]

Note that L[i] corresponds to the coefficient ai of x^i in f(x), for 0 <= i <= n.

Write a recursive function named poly that accepts the list of coefficients L
and a real number x_0 as arguments. It should return the polynomial evaluated
at the value x_0.

For example:
poly([1, 2, 3], 5) should return the value 1 + 2*5 + 3*(5^2) = 86.

You do not have to accept input from the user or print the output to the console.
You just have to write the function definition.'''

def poly(L, x_0):

    '''A recursive function to compute the value of a polynomial.

    Parameters:
    L: list of integers
    x_0: integer
    Return:
    result: integer'''

    if len(L) == 0:
        return 0
    return L[0] + x_0* poly(L[1:], x_0)