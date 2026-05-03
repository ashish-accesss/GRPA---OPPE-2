'''
If you have grasped the essence of recursion, then you would see the simplicity of the whole idea when you solve this problem. All those who have done Maths-2, or are doing Maths-2, should be able to appreciate this problem. If you are yet to do Maths-2, you can still try to attempt this problem. But we request learners not to be intimidated by the heavy use of notation. Feel free to skip this problem if it is perceived to be too hard.

Any square matrix M has a number associated with it called its determinant. The determinant of a 2 x 2 matrix is defined as follows:

det([[a, b],
    [c, d]]) = ad - bc

For any n x n square matrix M, its determinant is defined recursively as follows:

det(M) = sum from j=0 to n-1 of [(-1)^j * M[0][j] * Mj]

Here, Mj is the determinant of the matrix obtained by removing the 0th row and the jth column of M and 0 <= j < n. Here, we have used zero-based indexing.

For example, for a 3 x 3 matrix, we have:
det([[a, b, c],
    [d, e, f],
    [g, h, i]]) =
(+1)*a*det([[e, f],
            [h, i]]) 
- b*det([[d, f],
        [g, i]]) 
+ c*det([[d, e],
        [g, h]])

Write a recursive function named det that accepts a square matrix as argument and returns its determinant.

In the process of writing this function, it would be useful to look into GrPA-3 of week-7. A good approach would be to write two functions: det and minor_matrix.

You do not have to accept input from the user or print the output to the console. You just have to write the function definition.'''


def det (M):

    '''A recursive function to compute the determinant of M.

    Parameters:
    M: list of lists
    Return:
    result: integer'''

    n=len(M)
    if n == 1:
        return M[0][0]
    if n == 2:
        return M[0][0]*M[1][1] - M[0][1]*M[1][0]
    result=0
    for j in range(n):
        minor=[]
    for i in range(1,n):
        row =M[i][:j]+M[i][j+1:]
    minor.append(row)
    sign=(-1) ** j
    result+=sign*M[0][j]*det(minor)
    return result