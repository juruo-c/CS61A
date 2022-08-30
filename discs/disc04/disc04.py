"""
1.2 Tutorial: Consider a special version of the count_stairways problem,
where instead of taking 1 or 2 steps, we are able to take up to and including
k steps at a time.
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
"""
def count_k(n, k):
    """
    >>> count_k(3, 3) # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1) # Only one step at a time
    1   
    """
    if k == 1:
        return 1
    if n == 0:
        return 1
    cnt = 0
    for i in range(1, min(n + 1, k + 1)):
        cnt += count_k(n - i, k)
    return cnt

"""
2.2 Tutorial: Write a function that takes a list s and returns a new list
that keeps only the even-indexed elements of s and multiplies them by their
corresponding index.
"""
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

"""
2.3 Write a function that takes in a list and returns the maximum product that
can be formed using nonconsecutive elements of the list. The input list will
contain only numbers greater than or equal to 1.
"""
def max_product(s):
    """Return the maximum product that can be formed using non-consecutive
    elements of s.
    >>> max_product([10,3,1,9,2]) # 10 * 9
    90
    >>> max_product([5,10,5,10,5]) # 5 * 5 * 5
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    if len(s) == 1:
        return s[0]
    return max(max_product(s[1:]), s[0] * max_product(s[2:]))