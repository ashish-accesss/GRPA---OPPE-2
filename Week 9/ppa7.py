'''Write a recursive function named count that accepts the following arguments:

L: list of words
word: a word, could be any string
This function should return the number of occurrences of word in L.

(1) You cannot use the built-in count method for lists in this problem.

(2) All words will be in lower case.

(3) You do not have to accept input from the user or print the output to the console. You just have to write
the definition of both the functions.'''

def count(L, word):

    '''A recursive function to compute the frequency of occurrences of word in L.

    Parameters:
    L: list of words
    word: string
    Return:
    result: integer'''

    if len(L) == 0:
        return 0
    if L[0] == word:
        return 1+count(L[1:],word)
    return count(L[1:],word)