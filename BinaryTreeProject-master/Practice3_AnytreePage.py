# Binary Search Tree in Python
# Utilizing the Pycharm IDE

# ***Note: I like the format of the Anytree Python library, but am having trouble changing setting certain***
# functions up within it to reach my assignment goals (such as Find, Min, Max).

# reference: https://stackoverflow.com/questions/2358045/how-can-i-implement-a-tree-in-python
# http://pydoc.net/anytree/2.4.3/anytree.node.nodemixin/

# reference: https://anytree.readthedocs.io/en/latest/

from anytree import Node, RenderTree, Walker
from anytree import Node, RenderTree, AsciiStyle

layer1 = Node(44)
layer2_1 = Node(6, parent=layer1)
layer2_2 = Node(9, parent=layer1)
layer3_1 = Node(34, parent=layer2_2)
layer3_2 = Node(5, parent=layer2_1)
layer3_3 = Node(4, parent=layer2_1)


print('\nShowing the entire tree:')
for pre, fill, node in RenderTree(layer1):
    print("%s%s" % (pre, node.name))
print('\n')

w = Walker()

print('\nWalking the tree, layers3_2, and layers3_3:')
print(w.walk(layer3_2, layer3_3))
print('\n')

print('Showing the tree AsciiStyle:')
print(RenderTree(layer1, style=AsciiStyle()))
print('\n')



# reference: https://anytree.readthedocs.io/en/latest/