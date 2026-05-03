'''POINT CLASS PROBLEM

We are going to model points in 2D space as objects of a class named Point.

Mathematical details:
1) Distance of a point P(x, y) from the origin is:
√(x² + y²)

2) Slope of the line joining the origin and P is:
y / x   (for x ≠ 0)

--------------------------------------------------

Define a class named Point with the following specification:

ATTRIBUTES:
- x: int → x-coordinate of the point
- y: int → y-coordinate of the point

--------------------------------------------------

METHODS:

1) __init__(x, y)
- Constructor that initializes x and y

2) distance()
- Returns the distance of the point from the origin (float)

3) is_origin()
- Returns True if the point is (0, 0), otherwise False

4) on_xaxis()
- Returns True if the point lies on x-axis, otherwise False

5) on_yaxis()
- Returns True if the point lies on y-axis, otherwise False

6) quadrant()
- Returns the quadrant in which the point lies
- Possible outputs:
'first', 'second', 'third', 'fourth'
- Assume this is called only if the point is not on axes

7) slope()
- Returns slope of line joining origin and the point (float)
- Assume this is called only if the point is not on y-axis

--------------------------------------------------

NOTES:
- Each test case corresponds to one method call
- Use P to denote the object
- Do NOT take input from user
- Do NOT print anything
- Only define the class'''

