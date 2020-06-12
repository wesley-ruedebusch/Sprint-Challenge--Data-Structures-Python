"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""

# import Queue to support BFT
# from queue_copy import Queue
# # import Stack to support iterative DFT
# from stack_copy import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # is there a root? -- not actually needed
        # if self is None:
        #     # if no, first node
        #     self = BSTNode(value)
        # # else, compare value against it
        # else:
        # if less than,
        if value < self.value:
            # go left
            # check for another node
            if self.left:
                #then self.left is a node
               self.left.insert(value)
            else:
                self.left = BSTNode(value)
        # if greater than or equal,
        else:
            # go right
            # check for another node
            if self.right:
                #then self.right is a node
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if tree is empty
        if self is None:
            return False
        # check if self is the target
        elif self.value == target:
            return True
        elif target < self.value:
            if self.left:
               return self.left.contains(target)
            else:
                return False
        else:
            if self.right:
               return self.right.contains(target)
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self is None:
            return None
        elif self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        #check if there is anything in tree
        if self:
            fn(self.value)
            # cycle through left branches
            if self.left:
                self.left.for_each(fn)
            # cycle through right branches
            if self.right:
                self.right.for_each(fn)