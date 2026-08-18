""" An illustration of a binary tree structure."""
#################################################################################

from collections import deque    # for the 'level-order' traversal function.

#################################################################################

# Define the class and methods for the tree structure.
class Node:
    def __init__( self , data ):
        self.data        = data
        self.right_child = None
        self.left_child  = None

#################################################################################
# Define the various functions to traverse a binary tree.

def in_order( root_node ):
    """ A function to recursively perform an 'in_order' traversal of a binary tree."""
    current = root_node

    if current is None:
        return
    
    in_order( current.left_child )  # go down leftward, then back to the root
    print( current.data )           # print the ending node
    in_order( current.right_child ) # go down rightward, then back to the root


def pre_order( root_node ):
    """ A function to recursively perform a 'pre_order' traversal of a binary tree."""
    current = root_node
    
    if current is None:
        return
    
    print( current.data )            # print the current (root) node
    pre_order( current.left_child )  # go down leftward, then back to the root
    pre_order( current.right_child ) # go down rightward, then back to the root


def post_order( root_node ):
    """ A function to recursively perform a 'post_order' traversal of a binary tree."""
    current = root_node

    if current is None:
        return
    
    post_order( current.left_child )  # go down the left subtree, then print the end
    post_order( current.right_child ) # go down the right subtree, then print the end
    print( current.data )


def level_order( root_node ):
    """ A function to recursively perform a 'level_order' traversal of a binary tree."""
    list_of_nodes = []                      # an empty list

    traversal_queue = deque( [root_node] )  # put the nodes in a queue, making 'root_node' an iterable list.

    while len( traversal_queue ) > 0:       # as long as there are elements in the queue
        node = traversal_queue.popleft()    # dequeue (pop) a node
        list_of_nodes.append( node.data )   # add the node the the list (array)

        if node.left_child:                 # is there a left child
            traversal_queue.append( node.left_child )
            if node.right_child:
                traversal_queue.append( node.right_child )

    return list_of_nodes


#################################################################################
# Define and manipulate the tree structure.

# Define 4 nodes for the tree
n1 = Node( "root node" )
n2 = Node( "left child node" )
n3 = Node( "right child node" )
n4 = Node( "left grandchild node" )
n5 = Node ( "right-left grandchild" )
n6 = Node ( "right-right grandchild" )

# Now connect the nodes, essentially defining the 'edges'.
n1.left_child  = n2
n1.right_child = n3
n2.left_child  = n4
n3.left_child  = n5
n3.right_child = n6

# Traverse the 'left-subtree'.  Note this is only the left-most set of edges.
print( "\nThe left subtree is:" )
current = n1
while current:
    print( current.data )
    current = current.left_child

# Traverse the 'right-subtree'.  Note this is only the right-most set of edges.
print( "\nThe right subtree is:" )
current = n1
while current:
    print( current.data )
    current = current.right_child

# Traverse the tree using the 'in_order' function.
print( "\nTraversing the tree using the 'in_order' method." )
in_order( n1 )

# Traverse the tree using the 'pre_order' function.
print( "\nTraversing the tree using the 'pre_order' method." )
pre_order( n1 )

# Traverse the tree using the 'post_order' function.
print( "\nTraversing the tree using the 'post_order' method." )
post_order( n1 )

# Traverse the tree using the 'level_order' function.
print( "\nTraversing the tree using the 'level_order' method." )
print( level_order( n1 ) )

