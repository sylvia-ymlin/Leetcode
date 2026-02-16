# Given a sequence of numbers, determine if it is the pre-order traversal of some BST (Binary Search Tree) -- if yes, return 1, else 0
# Pre-order traversal: Root -> Left Subtree -> Right Subtree
# Constraints:
# - All values in left subtree < Root value
# - All values in right subtree > Root value
# i.e., BST pre-order traversal has a monotonic lower bound: once you enter a node's right subtree, subsequent values must be greater than that node's value
# i.e., you can go left getting smaller, but once go right getting larger, you cannot get smaller than that parent node --> so need stack for validation
# 
# Second task: Find values of the leftmost leaf node and rightmost leaf node of this tree
# If the found leaf node is the root itself, it means missing left or right subtree, output 0 for corresponding position

# Core Idea
# A stack: Simulate path from root to current node
# A lower_bound: Min allowed value for current node, initial value -1, because problem states all positive integers
# Algorithm flow:
# 1. First number is root, push to stack
# 2. Iterate nodes x from left to right
# -- If x < lower_bound, x violates BST rule, return 0
# -- If x > stack[-1], means x is in right subtree of stack top node
#    - Pop stack top nodes until stack top value > x
#    - For each popped node, update lower_bound to that node's value
# -- Push x to stack
# 3. Traversal ends, means valid BST pre-order, return 1

# To find leftmost and rightmost leaf nodes, can explicitly build the tree, then walk from root to left/right

# Build tree
class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

pre_order = list(map(int, input().split(" ")))

root = TreeNode(pre_order[0])

stack = [root] # Record current path
low_bound = -1 # Min value constraint
flag = True
for i in range(1, len(pre_order)):
    currentNode = TreeNode(pre_order[i])
    # Check if valid BST pre-order
    if currentNode.val < low_bound: # Smaller than min constraint, invalid
        flag = False
        break

    # Decreasing sequence, insert left child
    if stack and currentNode.val < stack[-1].val:
        # Current node is left child of stack top, insert directly
        stack[-1].left = currentNode
        stack.append(currentNode)
        continue

    # Stack empty, or current node > stack top, max means in right subtree
    # Need to pop all nodes smaller than current node from stack, finding parent of current node
    while stack and currentNode.val > stack[-1].val: # Pop all nodes smaller than current, last popped is parent
        parentNode = stack.pop()
        low_bound = parentNode.val # Update min constraint to popped node value
    
    # Mount right child; initially stack non-empty, parentNode must have value
    parentNode.right = currentNode 
    # Push current node
    stack.append(currentNode)

# Valid BST pre-order, build tree
if flag:
    leftNode = root
    # Find leftmost leaf node, left and right children are None
    while leftNode.left is not None or leftNode.right is not None:
        if leftNode.left is not None: # Prioritize left
            leftNode = leftNode.left
        else: # Go right
            leftNode = leftNode.right
    
    rightNode = root
    while rightNode.right is not None or rightNode.left is not None:
        if rightNode.right is not None:
            rightNode = rightNode.right
        else:
            rightNode = rightNode.left
    
    res = 1
    left_val = leftNode.val if leftNode != root else 0
    right_val = rightNode.val if rightNode != root else 0
    print(' '.join([str(res), str(left_val), str(right_val)]))
else:
    print(0)