"""
1.1 Write a function that takes two numbers m and n and returns their product.
Assume m and n are positive integers. Use recursion, not mul or *!
Hint: 5*3 = 5 + 5*2 = 5 + 5 + 5*1.
For the base case, what is the simplest possible input for multiply?
For the recursive case, what does calling multiply(m - 1, n) do? What
does calling multiply(m, n - 1) do? Do we prefer one over the other?
"""

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 1:
        return m 
    return m + multiply(m, n - 1)

"""
1.3 Tutorial: Recall the hailstone function from Homework 1. First, pick
a positive integer n as the start. If n is even, divide it by 2. If n is odd,
multiply it by 3 and add 1. Repeat this process until n is 1. Write a recursive
version of hailstone that prints out the values of the sequence and returns
the number of steps.
Hint: When taking the recursive leap of faith, consider both the return value
and side effect of this function.
"""

def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.
    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    print(n)
    if n == 1:
        return 1
    return 1 + hailstone(n // 2 if n % 2 == 0 else n * 3 + 1)

"""
1.4 Write a procedure merge(n1, n2) which takes numbers with digits in decreasing order and returns a single number with all of the digits of the two,
in decreasing order. Any number merged with 0 will be that number (treat
0 as having no digits). Use recursion.
Hint: If you can figure out which number has the smallest digit out of
both, then we know that the resulting number will have that smallest digit,
followed by the merge of the two numbers with the smallest digit removed.
"""

def merge(n1, n2):
    """ Merges two numbers
    >>> merge(31, 42)
    4321
    >>> merge(21, 0)
    21
    >>> merge (21, 31)
    3211
    """

"""
1.5 Tutorial: (Optional)
Define a function make fn repeater which takes in a one-argument function
f and an integer x. It should return another function which takes in one
argument, another integer. This function returns the result of applying f to
x this number of times.
Make sure to use recursion in your solution.
"""

def make_func_repeater(f, x):
    """
    >>> incr_1 = make_func_repeater(lambda x: x + 1, 1)
    >>> incr_1(2) #same as f(f(x))
    3
    >>> incr_1(5)
    6
    """
    def repeat(___________________):
        if _______________________:
            return __________________
        else:
            return __________________
    
    return _________________________

""" 
1.6 Below is the iterative version of is prime, which returns True if positive
integer n is a prime number and False otherwise:
def is_prime(n):
    if n == 1:
        return False
    k = 2   
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

Implement the recursive is prime function. Do not use a while loop, use
recursion. As a reminder, an integer is considered prime if it has exactly two
unique factors: 1 and itself
"""

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    def prime_helper(____________________):
        if ________________________:
            ________________________
        elif ________________________:
            ________________________
        else:
            ________________________

    return __________________________