'''Consider a spiral of semicircles. We start at a point Po on the x-axis with coordinates (1,0). The first arm of the spiral ends at P1 with coordinates
(r,0). The second arm of the spiral starts at Pi and ends at the center of the first arm, P2. The third arm starts from P2 and ends at P3 which
happens to be the center of the second arm. And finally, the fourth arm starts at P3 and ends at P4, the center of the third arm.
Write two functions named spiral_iterative and spiral_recursive, each of which accepts three arguments:

left: x-coordinate of the point Pb
right: x-coordinate of the point P1
n: the number of arms in the spiral
Both functions should return the the x-coordinate of Pn, the point at which the nth arm of the spiral ends.
You do not have to accept input from the user or print the output to the console. You just have to write the function definition.'''

def spiral_iterative(left, right, n):

    '''An iterative function to compute the x-coordinate of the nth arm of the spiral.

    Parameters:
    left: integer
    right: integer
    n: integer
    Return:
    result: float'''

    if n == 0:
        return left
    if n == 1:
        return right
    p0=left
    p1=right
    for _ in range(2,n+1):
        p2=(p0+p1)/2
    p0,p1=p1,p2
    return p1


def spiral_recursive(left, right, n):

    '''An recursive function to compute the x-coordinate of the nth arm of the spiral

        Arguments:
        left: integer
        right: integer
        n: integer
        Return:
        result: float'''

    if n == 0:
        return left
    if n == 1:
        return right
    return(spiral_recursive(left,right,n-1)+spiral_recursive(left,right,n-2))/2