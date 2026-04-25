""" Class definitions for queue operations using linked lists."""

""" Define the major queue classes and methods. """

#################################################################################
class Node( object ):
    """Define the 'node' class for each item in the queue."""
    def __init__( self, data=None, next=None, previous=None ):
        self.data     = data
        self.next     = next
        self.previous = previous

#################################################################################
class Queue:
    def __init__( self ):
        self.head  = None
        self.tail  = None
        self.count = 0


    def enqueue( self, data ):
        # The enqueue method adds a node item to the end of the queue.
        new_node = Node( data, None, None )

        if self.head == None:               # the queue is empty
            self.head = new_node
            self.tail = self.head
            
        else:
            new_node.previous = self.tail   # point to previous tail
            self.tail.next    = new_node    # the previous tail points to the new node
            self.tail         = new_node    # the new tail is the new node

        self.count += 1                     # bump the count of the items in the queue


    def dequeue( self ) :
        # The dequeue method removes a node from the front of the queue

        if self.count  == 1:                 # remove the only element in the queue
            self.head  = None
            self.tail  = None
            value      = self.data

        elif self.count > 1:
            self.head = self.head.next       # point the head to the 2nd element
            self.head.previous = None        # original head previous is now None
            value     = self.data

        elif self.count < 1:
            print( '\nThe queue is empty.' )
            return None

        self.count -= 1
        return value

