# practice page for creating minimum and maximum binary tree

# Binary Search Tree in Python
# Utilizing the Pycharm IDE

# ***Note: This tree works, and is not of my creation but is from the Github page shown below: ***
# https://github.com/joeyajames/Python/tree/master/Trees
# However, I still have to create a minimum/maximum for it.


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
        print("\nInserting", data)
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self, data):
        print("\nFinding", data, ":")
        if self.root:
            return self.root.find(data)
        else:
            return False

    def getHeight(self):
        print("\nObtaining the size of the tree:")
        if self.root:
            return self.root.getHeight()
        else:
            return 0

    def getSize(self):
        print("\nObtaining the height of the tree:")
        if self.root:
            return self.root.getSize()
        else:
            return 0

    def remove(self, data):
        # Taking a specific value (data) off of the tree

        print("\nRemoving", data, "from the tree:")
        if self.root is None:
            print('\nThis tree is empty.')
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

    def max(self):
        # Checking if the tree is empty

        print("\nChecking for the maximum data in the tree:")
        if self.root is None:
            print("\nThis tree is empty.")
            return False
        elif self.root.rightChild is None:
            print("\nThe root Node is the maximum value on the tree.")
        # Checking if the root node is the maximum value
        #if self.root.rightChild is not None and self.root.rightChild < self.root:
            #print("\nThe root Node", self.root, "is the maximum value on the tree.\n")

        # Checking the right side of the tree if it is not None
        elif self.root.rightChild is not None:

            originalRoot = self.root
            NodeParent = self.root
            childNode = self.root.rightChild
            while childNode.rightChild:
                NodeParent = childNode
                childNode = childNode.rightChild

                self.root.value = childNode.value
                #if childNode.rightChild:

                if NodeParent.value > childNode.value:
                    print("\nThe value ", NodeParent.value, "is the maximum number")
                    NodeParent.leftChild = childNode.rightChild

                elif childNode.value < NodeParent.value:
                    print("\nThe value of", NodeParent.value, "is the maximum value on the tree")
                    NodeParent.leftChild = None
                elif NodeParent.value < childNode.value:
                    print("\nChecking...")
                    NodeParent.rightChild = childNode.rightChild
                    if childNode.rightChild is None:
                        print("\nThe maximum value is", childNode.value, "on the right side of the tree...")

                else:
                    if NodeParent.rightChild is None:
                        return

def main():


    # setting the variable for the tree class
    bst = Tree()

    bst.remove(6)
    bst.max()

    bst.insert(10)
    bst.insert(5)
    bst.insert(7)
    bst.insert(30)
    bst.insert(41)
    bst.insert(100)
    bst.insert(98)
    bst.insert(300)
    bst.insert(31)

    print(bst.getHeight())
    print(bst.getSize())

    bst.preorder()

    bst.max()

    print(bst.find(7))

    print(bst.getHeight())
    print(bst.getSize())

    print(bst.remove(300))

    bst.preorder()

main()
