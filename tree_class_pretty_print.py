# This is to modify the print function of Tree class so that veritcal tree is printed.
# Beautiful vertical tree

from io import StringIO
# A StringIO is a file-like object that builds a string instead of printing
# anything out.

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
        self.pretty()
        return ''

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

    # Beautiful way to print a tree
    def height(self):
        """The height of a tree."""
        if self.is_leaf():
            return 0
        else:
            return 1 + max([b.height() for b in self.branches])

    def width(self):
        """Returns the printed width of this tree."""
        label_width = len(str(self.label))
        w = max(label_width,
                sum([t.width() for t in self.branches]) + len(self.branches) - 1)
        extra = (w - label_width) % 2
        return w + extra

    def pretty(self):
        """Print a tree laid out horizontally rather than vertically."""

        def gen_levels(tr):
            w = tr.width()
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
        h = self.height()
        g = gen_levels(self)
        next(g)
        for i in range(2*h + 1):
            next(g)
            print(file=out)
        print(out.getvalue(), end="")

if __name__ == '__main__':
    T = Tree(1, [Tree(2, [Tree(4), Tree(5)]), Tree(3, [Tree(6), Tree(7, [Tree(8), Tree(9)])])])
    print(T)
    #     1
    #  /    \
    #  2    3
    # / \ /  \
    # 4 5 6  7
    #       / \
    #       8 9
