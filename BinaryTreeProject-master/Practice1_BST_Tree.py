# Binary Search Tree in Python
# Utilizing the Pycharm IDE

# ***Note: This tree works, and is not of my creation but is from the Github page shown below: ***
# https://github.com/joeyajames/Python/tree/master/Trees
# I added a few minor changes such as print-statements to it, but have not created the maximum or minimum
# functions required for this assignment on this page.



# About Project: This project is called Project: Binary Search Tree for the course MS549.
# I will be implementing a Binary Search Tree (BST) utilizing the Python language for
# Phase 1 of the project implementing Add, Remove, Maximum, Minimum, InOrder, Traverse, and Find
# (with testing of each concept included).
# Then Phase 2 of the project will be to either write API documentation or video the project, and
# Phase 3 will be to establish trend lines.
# Phase 4 will be to compare/contrast time durations between insert and delete of Linked List and BST
# functionality.



# ________________________________________________________________________________________________
#Notes:

# reference: https://www.youtube.com/watch?v=YlgPi75hIBc
# bst = Tree()
# bst.insert(14)
# bst.preorder
# bst.postorder()
# bst.inorder()

# Tree() Class starts the commands; Tree() class utilizes Node() class that is invisible to the User
# (which has recursive functions that does the 'heavy lifting').
#reference: https://www.youtube.com/watch?v=YlgPi75hIBc
# ________________________________________________________________________________________________
# Overall page reference: https://www.youtube.com/watch?v=YlgPi75hIBc
# reference: https://github.com/joeyajames/Python/tree/master/Trees


class Node:
    def __init__(self, val):
        self.value = val
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        if self.value == data:
            return False

        elif self.value > data:
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def find(self, data):
        if (self.value == data):
            return True
        elif self.value > data:
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def getSize(self):
        if self.leftChild and self.rightChild:
            return 1 + self.leftChild.getSize() + self.rightChild.getSize()
        elif self.leftChild:
            return 1 + self.leftChild.getSize()
        elif self.rightChild:
            return 1 + self.rightChild.getSize()
        else:
            return 1

    def getHeight(self):
        if self.leftChild and self.rightChild:
            return 1 + max(self.leftChild.getHeight(), self.rightChild.getHeight())
        elif self.leftChild:
            return 1 + self.leftChild.getHeight()
        elif self.rightChild:
            return 1 + self.rightChild.getHeight()
        else:
            return 1

    # PreOrder (NLR - Node, Left, Right)
    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftChild:
                self.leftChild.preorder()
            if self.rightChild:
                self.rightChild.preorder()


    # Inorder (LNR - Left, Node, Right)
    def inorder(self):
        if self:
            if self.leftChild:
                self.leftChild.inorder()
            print(str(self.value))
            if self.rightChild:
                self.rightChild.inorder()

    # Postorder (LRN - Left, Right, Node)
    def postorder(self):
        if self:
            if self.leftChild:
                self.leftChild.postorder()
            if self.rightChild:
                self.rightChild.postorder()
            print(str(self.value))


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        if self.root:
            return self.root.getHeight()
        else:
            return 0

    def getSize(self):
        if self.root:
            return self.root.getSize()
        else:
            return 0

    def remove(self, data):
        # empty tree
        if self.root is None:
            return False

        # data is in root node
        elif self.root.value == data:
            if self.root.leftChild is None and self.root.rightChild is None:
                self.root = None
            elif self.root.leftChild and self.root.rightChild is None:
                self.root = self.root.leftChild
            elif self.root.leftChild is None and self.root.rightChild:
                self.root = self.root.rightChild
            elif self.root.leftChild and self.root.rightChild:
                delNodeParent = self.root
                delNode = self.root.rightChild
                while delNode.leftChild:
                    delNodeParent = delNode
                    delNode = delNode.leftChild

                self.root.value = delNode.value
                if delNode.rightChild:
                    if delNodeParent.value > delNode.value:
                        delNodeParent.leftChild = delNode.rightChild
                    elif delNodeParent.value < delNode.value:
                        delNodeParent.rightChild = delNode.rightChild
                else:
                    if delNode.value < delNodeParent.value:
                        delNodeParent.leftChild = None
                    else:
                        delNodeParent.rightChild = None

            return True

        parent = None
        node = self.root

        # find node to remove
        while node and node.value != data:
            parent = node
            if data < node.value:
                node = node.leftChild
            elif data > node.value:
                node = node.rightChild

        # case 1: data not found
        if node is None or node.value != data:
            return False

        # case 2: remove-node has no children
        elif node.leftChild is None and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = None
            else:
                parent.rightChild = None
            return True

        # case 3: remove-node has left child only
        elif node.leftChild and node.rightChild is None:
            if data < parent.value:
                parent.leftChild = node.leftChild
            else:
                parent.rightChild = node.leftChild
            return True

        # case 4: remove-node has right child only
        elif node.leftChild is None and node.rightChild:
            if data < parent.value:
                parent.leftChild = node.rightChild
            else:
                parent.rightChild = node.rightChild
            return True

        # case 5: remove-node has left and right children
        else:
            delNodeParent = node
            delNode = node.rightChild
            while delNode.leftChild:
                delNodeParent = delNode
                delNode = delNode.leftChild

            node.value = delNode.value
            if delNode.rightChild:
                if delNodeParent.value > delNode.value:
                    delNodeParent.leftChild = delNode.rightChild
                elif delNodeParent.value < delNode.value:
                    delNodeParent.rightChild = delNode.rightChild
            else:
                if delNode.value < delNodeParent.value:
                    delNodeParent.leftChild = None
                else:
                    delNodeParent.rightChild = None

    # PreOrder (NLR - Node, Left, Right)
    def preorder(self):
        if self.root is not None:
            print("\nPreOrder:")
            self.root.preorder()

    # Inorder (LNR - Left, Node, Right)
    def inorder(self):
        if self.root is not None:
            print("\nInOrder:")
            self.root.inorder()

    # Postorder (LRN - Left, Right, Node)
    def postorder(self):
        if self.root is not None:
            print("\nPostOrder:")
            self.root.postorder()

def main():

    # setting the variable for the tree class
    bst = Tree()

    print("\nInserting 10 (as main Node), then 5, 2, 7, and 30 into the tree.")
    bst.insert(10)
    bst.insert(5)
    bst.insert(2)
    bst.insert(7)
    bst.insert(30)
    print('\n')

    bst.preorder()
    bst.inorder()
    bst.postorder()

    print('\nHeight = ', bst.getHeight())
    print('\nSize = ', bst.getSize())

    print("\nShowing that the number 2 was removed:")
    print(bst.remove(2), '\n')


    bst.preorder()
    bst.inorder()
    bst.postorder()



main()
