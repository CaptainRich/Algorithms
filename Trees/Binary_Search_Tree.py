""" An illustration of a binary search tree."""
#################################################################################



#################################################################################

# Define the class and methods for the tree structure.

class Node:
    def __init__(self, data):
        self.data        = data     # a new node has data but no children
        self.right_child = None
        self.left_child  = None

class Tree:
    def __init__(self):
        self.root_node = None

    def insert( self, data ):
        ### Inserting must not violate the rules of a binary search tree.
        node = Node( data )

        if self.root_node is None:
            self.root_node = node   # the first/only node in the tree
            return self.root_node

        else:
            current = self.root_node  # 'current' tracks where a new node can be inserted
            parent  = None

            while True:
                parent = current
                if node.data < parent.data:
                    current = current.left_child  # new node is less, traverse left side
                    if current is None:           # no left child, add it
                        parent.left_child = node
                        return self.root_node

                else:
                    current = current.right_child  # new node is greater, traverse the right side
                    if current is None:            # no right child, add it
                        parent.right_child = node
                        return self.root_node

    def in_order( self, root_node ):
        # Define the 'in order' traversal function, which will dump (print) the tree.
        current = root_node

        if current is None:
            return

        self.in_order( current.left_child )
        print( current.data )
        self.in_order( current.right_child )



#####################################################################################################
# Exercise the binary tree functions.

tree = Tree()             # create the Tree object

n = tree.insert( 3 )
n = tree.insert( 7 )
n = tree.insert( 5 )
n = tree.insert( 4 )
n = tree.insert( 9 )
n = tree.insert( 1 )
n = tree.insert( 6 )

tree.in_order( n )


