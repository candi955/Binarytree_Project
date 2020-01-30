# 10,000 Numbers

# This page is part of phase 2 of the Binary Search Tree (BST) project, in which I will time various BST functions for time
# duration concerning the implementation of 100, 1000, 10000, and 100000 random numbers within a BST.

from binarytree import build
import numpy as np
import random
import time



# 10,000 Random Numbers
print("\nStarting a binary tree with 10,000 random numbers.\n\n")
randNums10000 = np.array(random.sample(range(1, 10001), 10000))
print(randNums10000)

# Putting 10,000 numbers in the tree
start10000 = time.time()
root = build(randNums10000)
end10000 = time.time()
duration10000 = end10000 - start10000
print(root)

# Deleting 10,000 numbers from the tree
deleteStart10000 = time.time()
root = build([])
endDeleteStart10000 = time.time()
durationDelete10000 = endDeleteStart10000 - deleteStart10000
print("\nPrinting the binary tree after emptying the list of/deleting 10,000 numbers: \n", root)

print("\nThe time duration to enter 10,000 random numbers into the Binary Search Tree is: ", duration10000, "seconds.")

print("\nThe time duration to delete 10,000 random numbers from the Binary Search Tree is: ", durationDelete10000, "seconds.")