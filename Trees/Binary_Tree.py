""" An illustration of a binary tree structure."""
#################################################################################

#################################################################################

# Define the class and methods for the tree structure.
class Node:
    def __init__( self , data ):
        self.data        = data
        self.right_child = None
        self.left_child  = None


#################################################################################
# Define and manipulate the tree structure.

# Define 4 nodes for the tree
n1 = Node( "root node" )
n2 = Node( "left child node" )
n3 = Node( "right child node" )
n4 = Node( "left grandchild node" )

# Now connect the nodes, essentially defining the 'edges'.
n1.left_child  = n2
n1.right_child = n3
n2.left_child  = n4

# Traverse the 'left-subtree'.
current = n1
while current:
    print( current.data )
    current = current.left_child

