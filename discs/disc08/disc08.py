class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

"""
2.1 Write a function that takes in a a linked list and returns the sum of all its elements.
You may assume all elements in lnk are integers.
"""
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    sum = 0
    while lnk is not Link.empty:
        sum += lnk.first
        lnk = lnk.rest 
    return sum 

"""
2.2 Write a function that takes in a Python list of linked lists and multiplies them
element-wise. It should return a new linked list.
If not all of the Link objects are of equal length, return a linked list whose length is
that of the shortest linked list given. You may assume the Link objects are shallow
linked lists, and that lst of lnks contains at least one linked list.
"""
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    # Note: you might not need all lines in this skeleton code
    multiplies = 1
    for lnk in lst_of_lnks:
        if lnk == Link.empty:
            return lnk
        multiplies *= lnk.first
    lst_of_rest = [lnk.rest for lnk in lst_of_lnks]
    return Link(multiplies, multiply_lnks(lst_of_rest))

"""
2.3 Tutorial: Write a recursive function flip two that takes as input a linked list lnk
and mutates lnk so that every pair is flipped.
"""
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk == Link.empty or lnk.rest == Link.empty:
        return
    lnk.first, lnk.rest.first = lnk.rest.first, lnk.first 
    flip_two(lnk.rest.rest)

"""
2.4 Tutorial: Implement filter link, which takes in a linked list link and a function
f and returns a generator which yields the values of link for which f returns True.
Try to implement this both using a while loop and without using any form of
iteration.
"""
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link != Link.empty:
        if f(link.first):
            yield link.first
        link = link.rest 
    """
    if link != Link.empty:
        if f(link.first):
            yield link.first
        yield from filter_link(link.rest, f)
    """
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    def is_leaf(self):
        return not self.branches
    def __repr__(self):
        return 'hhh'

"""
3.1 Define a function make even which takes in a tree t whose values are integers, and
mutates the tree such that all the odd integers are increased by 1 and all the even
integers remain the same.
"""
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2:
        t.label += 1
    for b in t.branches:
        make_even(b)

"""
3.2 Define a function square tree(t) that squares every value in the non-empty tree
t. You can assume that every value is a number.
"""
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    1
    >>> t.branches[0].branches[0].label
    9
    """
    t.label *= t.label
    for b in t.branches:
        square_tree(b)

"""
3.3 Tutorial: Define the procedure find paths that, given a Tree t and an entry,
returns a list of lists containing the nodes along each path from the root of t to
entry. You may return the paths in any order.
"""
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
    for b in t.branches:
        for path in find_paths(b, entry):
            paths.append([t.label] + path)
    return paths

"""
3.4 Write a function that combines the values of two trees t1 and t2 together with the
combiner function. Assume that t1 and t2 have identical structure. This function
should return a new tree.
Hint: consider using the zip() function, which returns an iterator of tuples where
the first items of each iterable object passed in form the first tuple, the second items
are paired together and form the second tuple, and so on and so forth.
"""
from operator import mul
def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    b = [combine_tree(b1, b2, combiner) for b1, b2 in zip(t1.branches, t2.branches)]
    return Tree(combiner(t1.label, t2.label), b)    

"""
3.5 Implement the alt tree map function that, given a function and a Tree, applies the
function to all of the data at every other level of the tree, starting at the root.
"""
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, dep):
        if dep % 2:
            label = map_fn(t.label)
        else:
            label = t.label 
        return Tree(label, [helper(b, dep + 1) for b in t.branches])
    return helper(t, 0)


    