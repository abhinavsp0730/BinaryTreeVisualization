"""
Program to calculate height of the binary tree.
        1 ------ level 1
       / \ 
      2   3 ------ level 2  (height of a binary tree is the deepest level, i.e 3)
     / \ 
    4   5 ------- level 3  height = 3
              
"""

# class to create binary tree
class Node:
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None 

# creating the above binary tree

# 1st level
root = Node(1)

# 2nd lwvwl
root.left = Node(2)
root.right = Node(3)

# 3rd level
root.left.left = Node(4)
root.left.right = Node(5)

def height(root):
    # height of the Null node is 0
    if not root:
        return 0
    # recursively calculating the height of the left subtree
    left_height = height(root.left)
    # recursively calculating the height of the right subtree
    right_height = height(root.right)
    
    # taking maximum value of left_height and right_height and adding 1 to it.
    # Think of the smallest subproblem i,e height of the leaf node,
    # having height = 1. So, our base case is gonna return 0 and
    # by adding 1 to it. It'll make the hieght of the leaf nodes to 1
    return (max(left_height, right_height) + 1 )
print(height(root))