# Binary Search Tree in Python
# Utilizing the Pycharm IDE

# Main reference, binarytree library documentation: https://readthedocs.org/projects/binarytree/downloads/pdf/latest/

# About Project: This project is called Project: Binary Search Tree for the course MS549.
# I will be implementing a Binary Search Tree (BST) utilizing the Python language for
# Phase 1 of the project implementing Add, Remove, Maximum, Minimum, InOrder, Traverse, and Find
# (with testing of each concept included).
# Then Phase 2 of the project will be to create BSTs and insertion/deletion function with random numbers.  Then I will
# either write API documentation or video the project.
# Phase 3 will be to establish trend lines of the time durations of insertion/deletion in Phase 2, and compare them
# with Arrays and Linked Lists from previous projects.
# Phase 4 will be to compare/contrast time durations between insert and delete of Linked List and BST
# functionality.


# ________________________________________________________________________________________________
# Other references used for research:
# https://stackabuse.com/search-algorithms-in-python/#binarysearch
# https://pypi.org/project/binarytree/
# https://pypi.org/project/binarytree/#description
# https://www.youtube.com/watch?v=YlgPi75hIBc
# reference: https://www.youtube.com/watch?v=YlgPi75hIBc

# Main reference, binarytree library documentation: https://readthedocs.org/projects/binarytree/downloads/pdf/latest/

from binarytree import Node


class Main():

    root = Node(34)

    root.right = Node(51)
    root.right.right = Node(55)
    root.right.left = Node(48)

    root.left = Node(29)
    root.left.left = Node(23)
    root.left.right = Node(31)

    print(root)

    print("Is the tree complete?: ", root.is_complete)
    print("Is the tree balanced?: ", root.is_balanced)
    print("What is the tree size?: ", root.size)
    print("What is the maximum value in the tree?: ", root.max_node_value)
    print("What is the minimum value in the tree?: ", root.min_node_value)
    print("The value of index 1 in the tree: ", root[1])
    print("The value of index 2 in the tree: ", root[2])
    print("The value of index 3 in the tree: ", root[3])
    print("The value of index 4 in the tree: ", root[4])
    print("The value of index 5 in the tree: ", root[5])
    print("The value of index 6 in the tree: ", root[6])
    print("Preorder (NLR - Node Left Right): ", root.preorder)
    print("Inorder (LNR - Left Node Right: ", root.inorder)
    print("Postorder (LRN - Left Right Node: ", root.postorder)
    print("Is the tree a Binary Search Tree: ", root.is_bst)

    print("Deleting index 4, which is the value", root[4], ".")
    root.__delitem__(4)
    print("Here is the updated Binary Search Tree: ", root)
    print("Is the tree a Binary Search Tree: ", root.is_bst)


Main()

# Main reference, binarytree library documentation: https://readthedocs.org/projects/binarytree/downloads/pdf/latest/