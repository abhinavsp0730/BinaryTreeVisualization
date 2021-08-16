"""
Program to print the nodes of the below binary tree by postorder traversal
        1 
       / \ 
      2   3
     / \ 
    4   5
              
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

def postorder(root):
    #base case: when we reach the leaf node
    if not root:
        return
    
    #traversing left subtree recursively
    postorder(root.left)
    #traversing right subtree recursively
    postorder(root.right)
    #printing the current node value
    print(root.val)

postorder(root)