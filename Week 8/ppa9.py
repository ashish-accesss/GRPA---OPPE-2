'''The scores of a class of students in the online degree program is represented as a CSV
file with the following header:

SeqNo, Name, Gender, CT,Python, PDSA
The name of the file is given by the variable filename. The first line will be the header.
The contents of the file will be in increasing order of sequence numbers.

Write a function named extract_lines that accepts filename as argument. Within the
function, read the file and look for all male students who have scored at least 70 marks
in Python. Copy these lines into a new file named python. csv. The entries in this file
should be in the increasing order of sequence numbers. Also, the first line of python. csv
should be the header, which is same as the one in filename.

(1) filename is a string variable that holds the filename. For example, in the first test
case, it is public_1. csv.

(2) You do not have to accept input from the console. You just have to write the function
definition.

(3) We shall be printing a random selection of five entries from python. csv.'''

def extract_lines(filename):

    '''Get all males who have scored at least 70 marks in Python

    Argument :
    filename: string
    Return:
    None'''
    