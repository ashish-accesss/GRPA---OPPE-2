'''Write a recursive function named power that accepts a square matrix A and a positive integer m as
arguments and returns Am.

You do not have to accept input from the user or print the output to the console. You just have to write the
function definition.'''
def multiply(A,B):
    n=len(A)
    result=[[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j]+=A[i][k] * B[k][j]
    return result

def power(A, m):

    '''A recursive function to compute A ** m.

    Parameters:
    A: list of lists
    m: integer
    Return:
    result: list of lists'''

    n=len(A)
    if m == 0:
        I =[[0]*n for _ in range(n)]
    for i in range(n):
        I[i][i]=1
    return I
    if m == 1:
        return A
    return multiply(A. power (A.m-1))