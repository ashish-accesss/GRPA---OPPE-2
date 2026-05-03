'''Write a function named primes_galore that accepts a list L of non-negative integers as argument and
returns the number of primes that are located at prime indices in L.

For example:

L = [1, 3, 11, 18, 17, 23, 6, 8, 10]

The prime indices in the list are 2, 3, 5, 7. Of these, there are prime numbers at the indices 2 and 5. Therefore,
the function should return the value 2 in this case.

You do not have to accept input from the user or print the output to the console. You just have to write the
function definition.'''
def primes_galore(L):

    '''Compute number of primes located at prime indices

    Argument:
        L: list of integers
    Return:
        result: integer'''

    def is_prime(n):
        if n<2:
            return False
        for i in range(2,int(n ** 0.5)+1):
            if n % i == 0:
                return False
            return True
    return sum(1 for i in range(len(L)) if is_prime(i) and is_prime(L[i]))