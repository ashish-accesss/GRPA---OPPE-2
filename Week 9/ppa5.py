'''Write a recursive function named palindrome that accepts a string word as argument
and returns True if it is a palindrome and False otherwise.

You do not have to accept input from the user or print the output to the console. You just
have to write the function definition.'''
def palindrome(word):

    '''A recursive function to determine if a string is a palindrome.

    Parameters:
    word: string
    Return:
    result: bool'''

    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return palindrome(word[1 :- 1])