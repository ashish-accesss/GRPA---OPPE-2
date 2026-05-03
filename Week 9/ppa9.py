'''Write a recursive function named uniq that accepts a non-empty list L as argument and returns a new list
after removing all duplicates from it. Your function must retain the last occurrence of each distinct element
in the list.

You do not have to accept input from the user or print the output to the console. You just have to write the
function definition.'''

def uniq(L):

    '''A recursive function to get unique elements from the list.

    Parameters:
    L: list
    Return:
    result: list
'''
    if len(L) == 0:
        return[]
    rest = uniq(L[1:])
    if L[0] in rest:
        return rest
    return [L[0]]+rest
