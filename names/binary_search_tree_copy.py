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

    # # Part 2 -----------------------

    # # Print all the values in order from low to high
    # # Hint:  Use a recursive, depth first traversal
    # def in_order_print(self, node):
    #     if node:
    #         node.in_order_print(node.left)
    #         print(node.value)
    #         node.in_order_print(node.right)

    #     # alt method
    #     # if self.left:
    #     #     self.left.in_order_print(node)
    #     # print(self.value)
    #     # if self.right:
    #     #     self.right.in_order_print(node)

    # # Print the value of every node, starting with the given node,
    # # in an iterative breadth first traversal
    # def bft_print(self, node):
    #     # create queue
    #     queue = Queue()

    #     # root into queue
    #     queue.enqueue(node)

    #     # while queue is not empty
    #     while queue.__len__() != 0:
    #         # node = pop head of queue
    #         node = queue.dequeue()
    #         # DO THE THING (print)
    #         print(node.value)
    #         # add children of root to queue
    #         if node.left:
    #             queue.enqueue(node.left)
    #         if node.right:
    #             queue.enqueue(node.right)

    #         ##### pop node off queue - cancel this one, we moved it up

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    # def dft_print(self, node):
    #     # create a stack
    #     stack = Stack()

    #     # root into stack
    #     stack.push(node)

    #     # while queue is not empty
    #     while stack.__len__() != 0:
    #         # node = pop head of stack
    #         node = stack.pop()
    #         # DO THE THING (print)
    #         print(node.value)
    #         # add children of root to stack
    #         if node.left:
    #             stack.push(node.left)
    #         if node.right:
    #             stack.push(node.right)

    # # Stretch Goals -------------------------
    # # Note: Research may be required

    # # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):

    #     if node:
    #         print(node.value)
    #         node.pre_order_dft(node.left)
    #         node.pre_order_dft(node.right)

    #     # TODO - Figure out why doens't this work,
    #     # when alt method of in_order_orint did?
    #     # print(self.value)
    #     # if self.left:
    #     #     self.left.in_order_print(node)
    #     # if self.right:
    #     #     self.right.in_order_print(node)

    # # Print Post-order recursive DFT
    # def post_order_dft(self, node):

    #     if node:
    #         node.post_order_dft(node.left)
    #         node.post_order_dft(node.right)
    #         print(node.value)