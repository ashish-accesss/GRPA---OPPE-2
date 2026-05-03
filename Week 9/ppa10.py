'''Write a recursive function named search that accepts the following arguments:

(1) L: a sorted list of integers

(2) k: integer

The function should return True if k is found in the list L, and False otherwise.

You do not have to accept input from the user or print output to the console. You just have to write the
function definition.'''

def search(L, k):

    '''A recursive function that searches for an element k in L.

    Parameters:
    L: list
    k: int
    Return:
    bool'''

    if len(L) == 0:
        return False
    if L[0] == k:
        return True
    return search(L[1:],k)