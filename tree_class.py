# This is an extension of learning from CS61A, tree recursion

# tree_recursion_tree.py summarized all the tree functions.

# This is to convert functional setup in tree_recursion_tree.py into a full Tree class which contains all the methods within.

# Use by:
# from ZCodeSnippets.tree_class import Tree

from class_link import Link

class Tree:
    """A tree is a label and a list of branches."""
    def __init__(self, label, branches=[]):
        self.label = label
        for branch in branches:
            assert isinstance(branch, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if self.branches:
            branch_str = ', ' + repr(self.branches)
        else:
            branch_str = ''
        return 'Tree({0}{1})'.format(self.label, branch_str)

    def __str__(self):
        return '\n'.join(self.indented())

    def indented(self):  # this is to recursively print a Tree.
        lines = []
        for b in self.branches:
            for line in b.indented():
                lines.append('  ' + line)
        return [str(self.label)] + lines
        # This is the original print_tree fucntion is a series of print() at different lines.
        # But __str__ requires to return a str object.

    # Set getter functions
    def get_label(self):
        return self.label

    def get_branches(self):
        return self.branches

    # Set bool function to tell whether it is a leaf
    # There is no need to tell whether it is a tree, because the object is created under the tree class.
    # Leaf has no branches, if it is not a leaf, then it must be a tree with branches.
    def is_leaf(self):
        """To tell whether the tree instance is a leaf or a tree with branches"""
        return not self.branches


    def count_nodes(self):
        """Return total number of nodes in this tree"""
        # return len(self.extract_nodes())
        return sum([1] + [b.count_nodes() for b in self.branches])

    def count_leaves(self):
        """Count the leaves of a tree"""
        if self.is_leaf():
            return 1
        else:
            return sum([b.count_leaves() for b in self.branches])


    def extract_nodes(self):
        """return a flat list contains all the nodes"""
        return [self.label] + sum([b.extract_nodes() for b in self.branches], [])


    def extract_leaves(self):
        """Return a list containing all the leaf labels of tree"""
        if self.is_leaf():
            return [self.label]
        else:
            return sum([b.extract_leaves() for b in self.branches], [])


    def increment_trees(self, n):
        """Return a tree like self but with every tree labels incremented of n"""
        return Tree(self.label + n, [b.increment_trees(n) for b in self.branches])


    def square_tree(self):
        """Return a tree with the square of every element in t"""
        return Tree(self.label **2, [b.square_tree() for b in self.branches])


    def increment_leaves(self, n):
        """Return a tree like self but with only leaf labels incremented of n """
        if self.is_leaf():
            return Tree(self.label + n)
        else:
            return Tree(self.label, [b.increment_leaves(n) for b in self.branches])


    def max_tree_v(self):
        """return the max labels in this tree"""
        return max([self.label] + [b.max_tree_v() for b in self.branches])
        # return max(self.extract_nodes())

    def max_leaf_v(self):
        """return the max leaf label in this tree"""
        return max(self.extract_leaves())


    def max_height(self):
        """Return the max height of a tree"""
        if self.is_leaf():
            return 1
        else:
            return 1 + max([b.max_height() for b in self.branches])

    def find_path(self, x):
        """Find path to the value x if x in the tree, else None"""
        if self.label == x:
            return [self.label]

        for path in [b.find_path(x) for b in self.branches]:
            if path:
                return [self.label] + path

    def finder(self, keywd):
        """Returns True if t contains a node with the value of keywd and False otherwise."""
        return self.label == keywd or True in [b.finder(keywd) for b in self.branches]
        # return keywd in self.extract_nodes()

    def sum_range(self):
        """Returns the range of the sums of t, that is:
        the difference between the largest and the smallest sums of t.
        return as a pair of value [min, max]
        """
        if self.is_leaf():
            return [self.label, self.label]
        else:
            min_v = min([b.sum_range()[0] for b in self.branches])
            max_v = max([b.sum_range()[1] for b in self.branches])
            x = self.label
            return [min_v + x, max_v + x]

    def prune(self, k):
        """Return a tree that takes in a tree only to the depth k"""
        if k == 0:
            return Tree(self.label)
        else:
            return Tree(self.label, [b.prune(k-1) for b in self.branches])

    def copy_tree(self):
        """Returns a copy of t. Only for testing purposes."""
        return Tree(self.label, [b.copy_tree() for b in self.branches])


    def replace_label(self, old, new):
        """replace a tree label to a new value is the value == old"""
        if self.label == old:
            return Tree(new, [b.replace_label(old, new) for b in self.branches])
        else:
            return Tree(self.label, [b.replace_label(old, new) for b in self.branches])

    def replace_leaf(self, old, new):
        """replace a leaf label to a new value is the value == old"""
        if self.is_leaf() and self.label == old:
            return Tree(new)
        else:
            return Tree(self.label, [b.replace_leaf(old, new) for b in self.branches])


    def sprout_leaves(self, vals):
        """Sprout new leaves containing the data in vals at each leaf in
        the original tree t and return the resulting tree."""
        if self.is_leaf():
            return Tree(self.label, [Tree(i) for i in vals])
        else:
            return Tree(self.label, [b.sprout_leaves(vals) for b in self.branches])


    def prune_repeats(self, seen=[]):
        """remove the tree in the branches that has shown before"""
        self.branches = [b for b in self.branches if b not in seen]
        seen.append(self)
        for b in self.branches:
            b.prune_repeats(seen)

    # Set basic calculation and comparison
    def __add__(self, other):
        """
        Add two tree together
        If a node at any particular position is present in one tree but not the other, it should be present in the new tree as well.
        """
        lab = self.label + other.label
        b1, b2 = self.branches, other.branches
        while len(b1) > len(b2):
            b2 = b2 + [Tree(0)]
        while len(b2) > len(b1):
            b1 = b1 + [Tree(0)]
        return Tree(lab, [b[0] + b[1] for b in zip(b1, b2)])

    def __eq__(self, other):
        return self.extract_nodes() == other.extract_nodes()
        # This method needs improvement
        # It will not show True if two tree is mirrored.

    # def all_paths(self):
    #     """return a list of Linked list that are all the paths in the tree
    #     need to use the Link class as well
    #     """
    #     paths = []
    #     if self.is_leaf():
    #         paths.append(Link(self.label))
    #     for b in self.branches:
    #         for path in b.all_paths():
    #             paths.append(Link(self.label, path))
    #     return paths  # can't not print all paths right away as it is a recursive function

    def all_paths(self):
        """to get all path of a tree in list form in a big list"""

        def helper(tree):
            """return a list of Linked list that are all the paths in the tree
            need to use the Link class as well
            """
            paths = []
            if tree.is_leaf():
                paths.append(tree.label)
            for b in tree.branches:
                for path in helper(b):
                    paths.append([tree.label, path])
            return paths  # can't not print all paths right away as it is a recursive function

        def flatten(lnk_lst):
            """To flatten a linked list like list in the form of:
            [a, [b, [c, d]]]
            return a flattened list in the form of:
            [a, b, c, d]
            """
            if isinstance(lnk_lst[1], list):
                return [lnk_lst[0]] + flatten(lnk_lst[1])
            else:
                return lnk_lst

        all_paths = helper(self)
        return [flatten(path) for path in all_paths]

    def convert_to_list(self):
        """This converts the tree strcture to a nested list type"""
        if self.is_leaf():
            return [self.label]
        else:
            tail = [b.convert_to_list() for b in self.branches]
            return [[self.label] + i for i in tail]


# Beautiful vertical tree
from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

def height(tree):
    """The height of a tree."""
    if tree.is_leaf():
        return 0
    else:
        return 1 + max([height(b) for b in tree.branches])

def width(tree):
    """Returns the printed width of this tree."""
    label_width = len(str(tree.label))
    w = max(label_width,
            sum([width(t) for t in tree.branches]) + len(tree.branches) - 1)
    extra = (w - label_width) % 2
    return w + extra

def pretty(tree):
    """Print a tree laid out horizontally rather than vertically."""

    def gen_levels(tr):
        w = width(tr)
        label = str(tr.label)
        label_pad = " " * ((w - len(label)) // 2)
        yield w
        print(label_pad, file=out, end="")
        print(label, file=out, end="")
        print(label_pad, file=out, end="")
        yield

        if tr.is_leaf():
            pad = " " * w
            while True:
                print(pad, file=out, end="")
                yield
        below = [ gen_levels(b) for b in tr.branches ]
        L = 0
        for g in below:
            if L > 0:
                print(" ", end="", file=out)
                L += 1
            w1 = next(g)
            left = (w1-1) // 2
            right = w1 - left - 1
            mid = L + left
            print(" " * left, end="", file=out)
            if mid*2 + 1 == w:
                print("|", end="", file=out)
            elif mid*2 > w:
                print("\\", end="", file=out)
            else:
                print("/", end="", file=out)
            print(" " * right, end="", file=out)
            L += w1
        print(" " * (w - L), end="", file=out)
        yield
        while True:
            started = False
            for g in below:
                if started:
                    print(" ", end="", file=out)
                next(g);
                started = True
            print(" " * (w - L), end="", file=out)
            yield

    out = StringIO()
    h = height(tree)
    g = gen_levels(tree)
    next(g)
    for i in range(2*h + 1):
        next(g)
        print(file=out)
    print(out.getvalue(), end="")


if __name__ == '__main__':
    T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
    print(T)
    # >>>
    # 1
    #   2
    #     4
    #     5
    #   3
    #     6
    #     7

    pretty(T)
    # >>>
    #    1
    #  /   \
    #  2   3
    # / \ / \
    # 4 5 6 7

    print(repr(T))
    # >>>
    # Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])

    print(T.get_label())     # >>> 1
    print(T.get_branches())  # >>> [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])]

    print(T.count_nodes())   # >>> 7
    print(T.count_leaves())  # >>> 4

    print(T.extract_nodes()) # >>> [1, 2, 4, 5, 3, 6, 7]
    print(T.extract_leaves())    # >>> [4, 5, 6, 7]

    print(T.increment_trees(2))
    # >>>
    # 3
    #   4
    #     6
    #     7
    #   5
    #     8
    #     9

    print(T.square_tree())
    # 1
    #   4
    #     16
    #     25
    #   9
    #     36
    #     49

    print(T.increment_leaves(2))

    # >>>
    # 1
    #   2
    #     6
    #     7
    #   3
    #     8
    #     9

    print(T.max_tree_v())  # >>> 7
    print(T.max_leaf_v())  # >>> 7

    print(T.max_height())  # >>> 3

    print(T.find_path(7))  # >>> [1, 3, 7]  # does not have to end at leaf

    print(T.finder(4)) # >>> True
    print(T.finder(10)) # >>> False

    print(T.sum_range()) # >>> [7, 11]

    print(T.prune(1))
    # >>>
    # 1
    #   2
    #   3

    T_copy = T.copy_tree()
    print(T_copy)
    # >>> same as T

    print(T.replace_label(2, 10))
    # >>>
    # 1
    #   10
    #     4
    #     5
    #   3
    #     6
    #     7

    print(T.replace_leaf(4, 10))
    # >>>
    # 1
    #   2
    #     10
    #     5
    #   3
    #     6
    #     7

    print(T.sprout_leaves([10, 20]))
    # >>>
    # 1
    #   2
    #     4
    #       10
    #       20
    #     5
    #       10
    #       20
    #   3
    #     6
    #       10
    #       20
    #     7
    #       10
    #       20

    print(T + T_copy)
    # >>>
    # 2
    #   4
    #     8
    #     10
    #   6
    #     12
    #     14

    print(T == T_copy) # >>> True

    # Print all paths
    X = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9)])])])
    print('\nX tree:')
    print(X)
    path_list = X.all_paths()
    print('All paths in X tree:')
    for i in path_list:
        print(i)
    print('')


    # T = Tree(1, [Tree(2, [Tree(4), Tree(5, [Tree(8), Tree(9)])]), Tree(3, [Tree(6), Tree(7)])])

    T0 = Tree(1)
    print('T0', T0.convert_to_list())

    T1 = Tree(1, [Tree(2), Tree(3)])
    print('T1', T1.convert_to_list())

    T2 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7)])])
    print('T2', T2.convert_to_list())

    T3 = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9), Tree(10)])])])
    print('T3', T3.convert_to_list())





# Other Tree related:

# Fibonacci tree setup by Tree class
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

def fib_tree(n):
    """A Fibonacci tree.

    >>> print(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    if n == 0 or n == 1:
        return Tree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return Tree(fib_n, [left, right])


if __name__ == '__main__':
    ft = fib_tree(6)
    print(ft)
    # >>>
    # 8
    #   3
    #     1
    #       0
    #       1
    #     2
    #       1
    #       1
    #         0
    #         1
    #   5
    #     2
    #       1
    #       1
    #         0
    #         1
    #     3
    #       1
    #         0
    #         1
    #       2
    #         1
    #         1
    #           0
    #           1
    ft.prune_repeats()
    print(ft)
    # >>>
    # 8
    #   3
    #     1
    #       0
    #       1
    #     2
    #   5
    #     2
    #     3
    #       2



# Binary trees

# A sub class of regular Tree, that defines the binary tree:
# A tree has exactly two branch, left and right

class BTree(Tree):
    """A tree with exactly two branches, which may be empty."""
    empty = Tree(None)

    def __init__(self, label, left=empty, right=empty):
        for b in (left, right):
            assert isinstance(b, BTree) or b is BTree.empty
        Tree.__init__(self, label, (left, right))

    @property
    def left(self):
        return self.branches[0]

    @property
    def right(self):
        return self.branches[1]

    def is_leaf(self):
        return [self.left, self.right] == [BTree.empty] * 2

    def __repr__(self):
        if self.is_leaf():
            return 'BTree({0})'.format(self.label)
        elif self.right is BTree.empty:
            left = repr(self.left)
            return 'BTree({0}, {1})'.format(self.label, left)
        else:
            left, right = repr(self.left), repr(self.right)
            if self.left is BTree.empty:
                left = 'BTree.empty'
            template = 'BTree({0}, {1}, {2})'
            return template.format(self.label, left, right)

if __name__ == '__main__':
    t = BTree(3, BTree(1),
                 BTree(7, BTree(5),
                          BTree(9, BTree.empty,
                                   BTree(11))))

    print(t)
    # >>>
    # 3
    #   1
    #     None
    #     None
    #   7
    #     5
    #       None
    #       None
    #     9
    #       None
    #       11
    #         None
    #         None



# Fib Tree by Binary tree
def fib_tree(n):
    """Fibonacci binary tree.

    >>> fib_tree(3)
    BTree(2, BTree(1), BTree(1, BTree(0), BTree(1)))
    """
    if n == 0 or n == 1:
        return BTree(n)
    else:
        left = fib_tree(n-2)
        right = fib_tree(n-1)
        fib_n = left.label + right.label
        return BTree(fib_n, left, right)

# Binary Search Tree
def bst(values):
    """Create a balanced binary search tree from a sorted list."""
    if not values:
        return BTree.empty
    mid = len(values) // 2
    left, right = bst(values[:mid]), bst(values[mid+1:])
    return BTree(values[mid], left, right)

def largest(t):
    """Return the largest element in a binary search tree.

    >>> largest(bst([1, 3, 5, 7, 9]))
    9
    """
    if t.right is BTree.empty:
        return t.label
    else:
        return largest(t.right)

# Second largest
def second(t):
    """Return the second largest element in a binary search tree.

    >>> second(bst([1, 3, 5]))
    3
    >>> second(bst([1, 3, 5, 7, 9]))
    7
    >>> second(Tree(1))
    """
    if t.is_leaf():
        return None
    elif t.right is BTree.empty:
        return largest(t.left)
    elif t.right.is_leaf():
        return t.label
    else:
        return second(t.right)

if __name__ == '__main__':

    t = bst([1, 3, 5, 7, 9, 11, 13])
    print(t)
    # >>>
    # 7
    #   3
    #     1
    #       None
    #       None
    #     5
    #       None
    #       None
    #   11
    #     9
    #       None
    #       None
    #     13
    #       None
    #       None


# Sets as binary search trees

def contains(s, v):
    """Return true if set s contains value v as an element.

    >>> t = BTree(2, BTree(1), BTree(3))
    >>> contains(t, 3)
    True
    >>> contains(t, 0)
    False
    >>> contains(bst(range(20, 60, 2)), 34)
    True
    """
    if s is BTree.empty:
        return False
    elif s.label == v:
        return True
    elif s.label < v:
        return contains(s.right, v)
    elif s.label > v:
        return contains(s.left, v)

def adjoin(s, v):
    """Return a set containing all elements of s and element v.

    >>> b = bst(range(1, 10, 2))
    >>> adjoin(b, 5) # already contains 5
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7)))
    >>> adjoin(b, 6)
    BTree(5, BTree(3, BTree(1)), BTree(9, BTree(7, BTree(6))))
    >>> contents(adjoin(adjoin(b, 6), 2))
    [1, 2, 3, 5, 6, 7, 9]
    """
    if s is BTree.empty:  # If empty then add it at the end of a leaf
        return BTree(v)
    elif s.label == v:    # If a label is v, then it is already there
        return s
    elif s.label < v:
        return BTree(s.label, s.left, adjoin(s.right, v))
    elif s.label > v:
        return BTree(s.label, adjoin(s.left, v), s.right)


# Factor tree
def factor_tree(n):
    """
    Returns a factor tree.
    Recall that in a factor tree, multiplying the leaves together is the prime factorization of the root, n
    """
    for i in range(2, n):
        if n % i == 0:
            return Tree(n, [factor_tree(i), factor_tree(n // i)])
    return Tree(n)

if __name__ == '__main__':
    print(factor_tree(20))
    # >>>
    # 20
      # 2
      # 10
        # 2
        # 5



# Containing search
def contains(elem, n, t):
    """
    >>> t1 = Tree(1, [Tree(1, [Tree(2)])])
    >>> contains(1, 2, t1)
    True
    >>> contains(2, 2, t1)
    False
    >>> contains(2, 1, t1)
    True
    >>> t2 = Tree(1, [Tree(2), Tree(1, [Tree(1), Tree(2)])])
    >>> contains(1, 3, t2)
    True
    >>> contains(2, 2, t2) # Not on a path
    False
    """
    if n == 0:
        return True
    elif t.is_leaf() and n == 1:
        return t.label == elem
    elif t.label == elem:
        return True in [contains(elem, n - 1, b) for b in t.branches]
    else:
        return True in [contains(elem, n, b) for b in t.branches]



# Siblings
def siblings(t):
    """Return a list of the labels of all nodes that have siblings in t.
    >>> a = Tree(4, [Tree(5), Tree(6), Tree(7, [Tree(8)])])
    >>> siblings(Tree(1, [Tree(3, [a]), Tree(9, [Tree(10)])]))
    [3, 9, 5, 6, 7]
    """
    result = [b.label for b in t.branches if len(t.branches) > 1]
    for b in t.branches:
        result += siblings(b)
    return result


# Implement the Sib class that inherits from Tree.
# In addition to label and branches, a Sib instance t has an attribute siblings that stores the number of siblings t has in Sib trees containing t as a node.
# Assume that the branches of a Sib instance will never be mutated or re-assigned.

class Sib(Tree):
    """A tree that knows how many siblings it has.
    >>> a = Sib(4, [Sib(5), Sib(6), Sib(7, [Sib(8)])])
    >>> a.label
    4
    >>> a.branches[1].label
    6
    >>> a.siblings
    0
    >>> a.branches[1].siblings
    2
    """
    def __init__(self, label, branches=[]):
        Tree.__init__(self, label, branches)
        self.siblings = 0
        for b in self.branches:
            b.siblings = len(self.branches) - 1
