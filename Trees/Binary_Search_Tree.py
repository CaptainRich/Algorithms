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
                    
    #################################################################################################
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
                    
    #################################################################################################
    def in_order_print( self, root_node ):
        # Define the 'in order' traversal function, which will dump (print) the tree.
        current = root_node

        if current is None:
            return

        self.in_order_print( current.left_child )
        print( current.data )
        self.in_order_print( current.right_child )
                    
    #################################################################################################
    def binary_search( self, data ):
        # A function to search a binary tree for a specified value.
        current = self.root_node
        print( "\nStarting binary search at: ", current.data )

        while True:
            if current is None:
                print( "Search item", data, "was not found." )
                return None

            elif current.data is data:
                print( "Search item found: ", data, "." )
                return data

            elif current.data > data:
                current = current.left_child

            else:
                current = current.right_child

                    
    #################################################################################################
    def get_node_with_parent( self, data ):
        # A helper function to find a specific node in the tree with a reference to its parent node.
        parent = None

        current = self.root_node

        if current is None:
            return( parent, None )

        while True:
            if current.data == data:
                # Found the node, return it with its parent.
                return( parent, current )

            elif current.data > data:
                # Move down the left hand branch
                parent  = current
                current = current.left_child

            else:
                # Move down the right hand branch
                parent  = current
                current = current.right_child

        return( parent, current )

                    
    #################################################################################################
    def remove_node( self, data ):
        # The function to delete a node from a binary tree.
        print( '\n Attempting to remove node: ', data )

        parent, node = self.get_node_with_parent( data )
       

        if parent is None and node is None:
            return False

        # Get the count of the node's children
        child_count = 0

        if node.left_child and node.right_child:
            child_count = 2

        elif (node.left_child is None) and (node.right_child is None):
            child_count = 0

        else:
            child_count = 1

        # Once the number of children are known, delete accordingly.
        print( '\n The number of child nodes is: ', child_count )

        if child_count == 0:
            # There are no children of this node.
            if parent:
                if parent.right_child is node:
                    parent.right_child = None
                else:
                    parent.left_child = None
            else:
                # If there is no parent, we're deleting the root node and tree
                self.root_node = None

        elif child_count == 1:
            next_node = None        # the child of the node to be deleted

            if node.left_child:
                next_node = node.left_child
            else:
                next_node = node.right_child

            if parent:
                if parent.left_child is node:
                    parent.left_child = next_node
                else:
                    parent.right_child = next_node
            else:
                # If no parent, reset it to the current node.
                self.root_node = next_node

        else:
            # The node to be deleted has two children
            parent_of_leftmost_node = node
            leftmost_node = node.right_child

            while leftmost_node.left_child:
                parent_of_leftmost_node - leftmost_node
                leftmost_node = leftmost_node.left_child

            node.data = leftmost_node

 
    ################################################################################################  
    def find_min_node( self ):
        # Find the minimum node in the tree, which is the bottom leftmost node.
        current = self.root_node
        if current is None:
                print('\n The tree is empty.' )

        while current.left_child:
            current = current.left_child

        return current.data          # no child, therefore the minimum node
 
    ################################################################################################  
    def find_max_node( self ):
        # Find the maximum node in the tree, which is the bottom rightmost node.
        current = self.root_node
        if current is None:
            print('\n The tree is empty.' )

        print( '\n Starting search for max node at: ', current.data )

        while current.right_child:
            current = current.right_child
            print( '\n The next right child is: ', current.data )

        return current.data          # no child, therefore the maximum node
        

        

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


tree.in_order_print( n )

# Search the tree for "4", which does exist.
tree.binary_search( 4 )

# Search the tree for "8", which does not exist.
tree.binary_search( 8 )

# Setup a 2nd tree to test the "delete node" operation.
tree2 = Tree()

m = tree2.insert( 5 )
m = tree2.insert( 2 )
m = tree2.insert( 7 )
m = tree2.insert( 9 )
m = tree2.insert( 1 )

tree2.in_order_print( m )

print( '\n The minimum node is:', tree2.find_min_node() )
print( '\n The maximum node is:', tree2.find_max_node() )

tree2.binary_search( 9 )
tree2.remove_node( 9 )
tree2.binary_search( 9 )



