'''COLLATZ FUNCTION PROBLEM

The Collatz function is defined for a positive integer n as:

    f(n) = 3n + 1   (if n is odd)
    f(n) = n / 2    (if n is even)

We repeatedly apply this function starting from n, forming a sequence:

    f(n), f(f(n)), f(f(f(n))), ...

It is believed that for any starting value of n, the sequence will always reach 1.

--------------------------------------------------

EXAMPLE (n = 10):

Step 1: 10 → 5
Step 2: 5  → 16
Step 3: 16 → 8
Step 4: 8  → 4
Step 5: 4  → 2
Step 6: 2  → 1

So, it takes 6 steps to reach 1.

--------------------------------------------------

TASK:

Write a recursive function:

    def collatz(n):

where:
- n is a positive integer (1 < n ≤ 32000)

The function should return:
- The number of times the function f must be applied
to reach 1 for the first time.

--------------------------------------------------

NOTE:
- Do NOT take input from the user
- Do NOT print anything
- Only return the result'''



def collatz(n):
    """
    A recursive function to compute the number of calls to the Collatz function of n

    Argument:
        n: integer
        Assume that 1 < n <= 32,000
    Returns: 
        result: integer
    """
    if n==1:
        return 0
    if n%2==0:
        return 1+collatz(n//2)
    else:
        return 1+collatz(3*n+1)