""" Class definitions for stack operations using linked lists."""


"""The 'Node' class defines each item/entry in the (single linked) list."""
class Node:
    """ Initializer / Constructor"""
    def __init__ ( self, data=None ):
        self.data = data
        self.next = None         # the end of the list is 'none'

class Stack:
    """ Initializer / Constructor"""
    def __init__( self ):
        self.top  = None
        self.size = 0            # the stack size is zero


#################################################################################
    def push( self, data ):
        # Define the operation of pushing a value onto the stack.

        # Create the new node for the stack (list).
        node = Node( data )

        if self.top:
            # The stack is not empty, add the node and update the pointers
            node.next = self.top    # point to previous top of stack
            self.top  = node        # the new top is the new node

        else:
            # For an empty stack, point to the new node
            self.top = node
        
        self.size += 1              # increment the size of the stack


#################################################################################
    def pop( self ):
        # Define the operation of popping a value off of the stack.

        if self.top :               # the stack is not empty
            data = self.top.data
            self.size -= 1

            if self.top.next:       # there are more nodes
                self.top = self.top.next   # point to the next node in the stack

            else:
                self.top = None
            
            return data
        
        else:
            print( '\nThe stack is empty, nothing to pop.' )


#################################################################################
    def peek( self ):
        # Define the "peek" operation, which returns the top of stack, without
        # altering the stack.

        if self.top:
            return self.top.data
        
        else:
            print( '\nThe stack is empty.' )
            return None

#################################################################################
    def print_st( self ):
        # Print the contents of the stack.
        current = self.top

        if not current:
            print( '\nCannot print an empty stack.' )
            return

        while current:
            print('Stack element is: ', current.data )
            current = current.next