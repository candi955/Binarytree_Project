# 100,000 Numbers

# This page is part of phase 2 of the Binary Search Tree (BST) project, in which I will time various BST functions for time
# duration concerning the implementation of 100, 1000, 10000, and 100000 random numbers within a BST.

from binarytree import build
import numpy as np
import random
import time


# 100,000 Random Numbers
print("\nStarting a binary tree with 100,000 random numbers.\n\n")
randNums100000 = np.array(random.sample(range(1, 100001), 100000))
print(randNums100000)

# Putting 100,000 numbers in the tree
start100000 = time.time()
root = build(randNums100000)
end100000 = time.time()
duration100000 = end100000 - start100000
print(root)

# Deleting 100,000 numbers from the tree
deleteStart100000 = time.time()
root = build([])
endDeleteStart100000 = time.time()
durationDelete100000 = endDeleteStart100000 - deleteStart100000
print("\nPrinting the binary tree after emptying the list of/deleting 100,000 numbers: \n", root)

print("\nThe time duration to enter 100,000 random numbers into the Binary Search Tree is: ", duration100000, "seconds.")

print("\nThe time duration to delete 100,000 random numbers from the Binary Search Tree is: ", durationDelete100000, "seconds.")