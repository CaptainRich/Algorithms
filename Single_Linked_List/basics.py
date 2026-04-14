""" The base class and functions to manipulate the 
    single linked list. """





####################################################################################################
####################################################################################################
"""The 'Node' class defines each item/entry in the (single linked) list."""

class Node:
    """ Initializer / Constructor"""
    def __init__ (self, data=None):
        self.data = data
        self.next = None         # the end of the list is 'none'

class SinglyLinkedList:
    """ Initialize a singly linked list. """
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

    def append( self, data ):
        # Encapsulate the data in a Node.
        node = Node( data )
        if self.tail:       # add at the end of the list
            self.tail.next = node
            self.tail = node

        else:               # the first entry in an empty list
            self.head = node
            self.tail = node
