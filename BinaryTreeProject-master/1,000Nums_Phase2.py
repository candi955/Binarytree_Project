# 1,000 Numbers

# This page is part of phase 2 of the Binary Search Tree (BST) project, in which I will time various BST functions for time
# duration concerning the implementation of 100, 1000, 10000, and 100000 random numbers within a BST.

from binarytree import build
import numpy as np
import random
import time


# 1,000 Random Numbers
print("\nStarting a binary tree with 1,000 random numbers.\n\n")
randNums1000 = np.array(random.sample(range(1, 1001), 1000))
print(randNums1000)

# Putting 1,000 numbers in the tree
start1000 = time.time()
root = build(randNums1000)
end1000 = time.time()
duration1000 = end1000 - start1000
print(root)

# Deleting 1,000 numbers from the tree
deleteStart1000 = time.time()
root = build([])
endDeleteStart1000 = time.time()
durationDelete1000 = endDeleteStart1000 - deleteStart1000
print("\nPrinting the binary tree after emptying the list of/deleting 1,000 numbers: \n", root)

print("\nThe time duration to enter 1,000 random numbers into the Binary Search Tree is: ", duration1000, "seconds.")

print("\nThe time duration to delete 1,000 random numbers from the Binary Search Tree is: ", durationDelete1000, "seconds.")