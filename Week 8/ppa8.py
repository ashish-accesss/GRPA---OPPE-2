'''The scores of a class of students in the online degree program is represented as a CSV
file with the following header:

Name, Gender, CT, Python, PDSA
The name of the file is given by the variable filename. The first line will be the header.

Write a function named improvement which accepts the filename as argument. It
should return the number of students whose scores have increased across the three
courses. That is, the number of students whose scores are in this order: CT < Python <
PDSA.

(1) filename is a string variable that holds the filename. For example, in the first test
case, it is public_1. txt.

(2) You do not have to accept input from the console. You just have to write the function
definition.'''

def improvement(filename):

    '''Find all students who have shown an improvement

    Argument:
    filename: string, path to file
    Return:
    count: integer'''
    