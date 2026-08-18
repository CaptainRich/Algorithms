""" An implementation of 'Reverse Polish' notation using a tree structure."""
#################################################################################


class TreeNode:
    def __init__ ( self, data=None ):
        self.data  = data
        self.right = None
        self.left  = None


class Stack:
    def __init__ ( self ):
        self.elements = []

    def push( self, item ):
        self.elements.append( item )

    def pop( self ):
        return self.elements.pop()

#################################################################################
# Define the evaluation function.  Note this is a recursive function.

def calc( node ):
    if node.data == "+":
        return calc( node.left ) + calc( node.right )

    elif node.data == "-":
        return calc( node.left ) - calc( node.right )

    elif node.data == "*":
        return calc( node.left ) * calc( node.right )

    elif node.data == "/":
        return calc( node.left ) / calc( node.right )

    else:
        return node.data   # just return an operand


#################################################################################
# Define the expression to operate on and setup the stack.

expr = "4 5 + 5 3 - *".split()   # this yields "expr" as a list
stack = Stack()

# Build the tree.
for term in expr:
    if term in "+-*/":             # if we have an operator, pop its operands
        node = TreeNode( term )
        node.right = stack.pop()
        node.left  = stack.pop()

    else:
        node = TreeNode( int( term ) ) # otherwise push an operand

    stack.push( node )

# Generate the result of the expression
root = stack.pop()
result = calc( root )
print( "/nThe result of '4 5 + 5 3 - *' is: ", result )
