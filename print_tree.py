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

    def is_leaf(self):
        """To tell whether the tree instance is a leaf or a tree with branches"""
        return not self.branches


# __str__ method 调用了 indented函数, 就是把树打印出来的方法.
if __name__ == '__main__':
    X = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9)])])])
    print(X)
    # >>>
    # 1
    #   2
    #     4
    #     5
    #   3
    #     6
    #     7
    #       8
    #       9


# 另一种打印方法, 由3个函数组成, 不是Tree Class的内部方法
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
    X = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9)])])])
    pretty(X)
    #     1    
    #  /    \  
    #  2    3  
    # / \ /  \ 
    # 4 5 6  7 
    #       / \
    #       8 9
