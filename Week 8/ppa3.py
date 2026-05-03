'''Write a function named get_max_line that accepts a text file named filename as argument. Each line in this file contains an integer. The function should return the line number that houses the maximum integer in the file. If multiple lines have the same maximum number, return the smaller of the two. Line numbers start from one and not zero.

(1) filename is a string variable that holds the name of the file. For example, in the first test case, it is filename = 'public_1.txt'.

(2) You do not have to accept input from the console or print the output. You have to write the function definition.'''
def get_max_line(filename):

    '''Get the line that houses the maximum value

    Argument :
    filename: string, path to the file
    Return:
    result: integer'''
    