'''(1) Write a function named insert that accepts a sorted list L of integers and an integer x as arguments. It
should return a sorted list with the element x inserted into the input list at the right place.

(2) Write a recursive function named isort that accepts a non-empty list L of integers as argument. It
should return a sorted list in ascending order. isort must make use of insert. This is a popular sorting
algorithm and is called insertion sort.

(1) Each test case corresponds to one function call.

(2) You do not have to accept input from the user or print the output to the console. You just have to write
the definition of both the functions.

(3) You cannot use any built-in sort functions or methods in this problem.'''

def insert(L, x):

    '''Insert x in L

    Parameters:
    L: list of sorted integers
    x: integer
    Return:
    result: sorted list of integers'''

    if L == []:
        return [x]
    if x <= L[0]:
        return [x]+L
    return [L[0]] + insert(L[1:],x)

def isort(L):

    '''A recursive function to sort the list L

    Arguments:
    L: list of integers
    Return:
    result: sorted list of integers'''

    if len(L) <= 1:
        return L
    return insert((isort(L[1:]), L[0]))