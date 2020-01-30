# 100 Numbers
# Main reference: https://readthedocs.org/projects/binarytree/downloads/pdf/latest/

# This page is part of phase 2 of the Binary Search Tree (BST) project, in which I will time various BST functions for time
# duration concerning the implementation of 100, 1000, 10000, and 100000 random numbers within a BST.

from binarytree import build
import numpy as np
import random
import time


# 100 Random Numbers
print("\nStarting a binary tree with 100 random numbers.\n\n")
randNums100 = np.array(random.sample(range(1, 101), 100))
print(randNums100)

# Putting 100 numbers in the tree
start100 = time.time()
root = build(randNums100)
end100 = time.time()
duration100 = end100 - start100
print(root)

# Deleting 100 numbers from the tree
deleteStart100 = time.time()
root = build([])
endDeleteStart100 = time.time()
durationDelete100 = endDeleteStart100 - deleteStart100
print("\nPrinting the binary tree after emptying the list of/deleting 100 numbers: \n", root)

print("\nThe time duration to enter 100 random numbers into the Binary Search Tree is: ", duration100, "seconds.")

print("\nThe time duration to delete 100 random numbers from the Binary Search Tree is: ", durationDelete100, "seconds.")