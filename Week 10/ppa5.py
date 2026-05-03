'''VECTOR CLASS PROBLEM

A vector in 2D space corresponding to the point P(x, y) has one end at the origin
and the other end at point P.

We are interested in the following operations on a vector:

--------------------------------------------------

SCALING:
A vector can be scaled by a number s.
Example:
[x, y] → [s*x, s*y]

--------------------------------------------------

REFLECTION:
- Reflection about Y-axis:
[x, y] → [-x, y]

- Reflection about X-axis:
[x, y] → [x, -y]

--------------------------------------------------

ADDITION:
Two vectors [a, b] and [c, d] can be added:
[a + c, b + d]

--------------------------------------------------

TASK:

Define a class named Vector with the following specification:

ATTRIBUTES:
- x: int → first coordinate of the vector
- y: int → second coordinate of the vector

--------------------------------------------------

METHODS:

1) __init__(x, y)
- Constructor that initializes x and y

2) print_info()
- Print coordinates in the format: (x,y)
- No spaces allowed
- Do NOT return anything

3) scale(s)
- Scale the vector by s units
- Update current vector

4) reflect_about_x()
- Reflect vector about X-axis

5) reflect_about_y()
- Reflect vector about Y-axis

6) add(other)
- Takes another vector as input
- Returns a NEW Vector which is the sum

--------------------------------------------------

NOTES:
- Each test case may call one or more methods
- Use V to denote the object
- Do NOT take input from user
- Do NOT print anything except in print_info()
- Only define the class'''

