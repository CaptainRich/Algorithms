""" The base class and functions to manipulate the 
    doubly linked list. """

####################################################################################################
####################################################################################################
"""The 'Node' class defines each item/entry in the (doubly linked) list."""

class Node:
    """ Initializer / Constructor"""
    def __init__ (self, data=None, next=None, previous=None):
        self.data     = data
        self.next     = next
        self.previous = previous
       

class DoublyLinkedList:
    """ Initialize a singly linked list. """
    def __init__ (self):
        self.head = None
        self.tail = None
        self.size = 0

##################################################################################
    def iter( self ):
        # This function is a 'generator' saving its state between calls.
        current = self.head
        
        while current:
            val = current.data
            current = current.next  # move on to the next item in the list
            yield val

##################################################################################
    def append_at_start( self, data ):
        # This function appends a new node at the start of the doubly linked list.
        new_node = Node( data, None, None )

        if self.head is None:              # New list, nothing exists yet
            self.head = new_node
            self.tail = self.head

        else:                              # The list exists
            new_node.next      = self.head
            self.head.previous = new_node
            self.head          = new_node

        self.size += 1

        

##################################################################################
    def append( self, data ):
        # Encapsulate the data in a Node.
        new_node = Node( data, None, None )

        if self.head is None:                # add the new node to an empty list
            self.head = new_node
            self.tail = self.head

        else:                                # the list exists, append at the end
            new_node.previous = self.tail    # new previous is set to existing tail
            self.tail.next    = new_node
            self.tail         = new_node

        self.size += 1

##################################################################################
    def append_at_a_location( self, data ):
        # This routine inserts a node in a doubly linked list where the node being
        # added matches existing data in the list.

        # Start at the 'head' and traverse to the node with matching data.
        current  = self.head
        previous = self.head

        # Encapsulate the new data into a node.
        new_node = Node( data, None, None )

        while current:
            if current.data == data:               # found the insertion point
                new_node.previous = previous       # insert before the existing node
                new_node.next     = current
                previous.next     = new_node
                current.previous  = new_node
                self.size         += 1

            previous = current                     # if not the right node, move forward
            current  = current.next

##################################################################################
    def list_size( self) :
        # No need toy traverse the list, just return the size.

        return self.size

##################################################################################
    def search( self, data ):
        # Search the list for a specific data item.
        for node in self.iter( ):
            if data == node:
                return True
            
        return False

#################################################################################
    def delete_node_on_data( self , data ):
        # Routine to delete a node from  the list, if 'data' matches
        current  = self.head      #
        node_deleted = False

        if current == None:
            # The list is empty
            print( 'The list is empty, nothing to delete.' )

        elif current.data == data:
            # Have found the node to delete at the start of the list
            self.head.previous = None
            self.head          = current.next
            node_deleted       = True

        elif self.tail.data == data:
            # Have found the node to delete at the tail of the list
            self.tail      = self.tail.previous
            self.tail.next = None
            node_deleted   = True

        else:
            # The node to delete could be in the middle of the list
            while current:
                # Search for the matching node
                if current.data == data:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    node_deleted = True
                    break

                else:
                    current = current.next  # keep searching

            if node_deleted == False:
                print( 'Desired item is not in the list.' )

        if node_deleted:
            self.size -= 1

#################################################################################
    def delete_node_on_location( self, index ):
        # Start at the 'head' and traverse to 'index', then delete the node
        current  = self.head
 
        count = 1
        while current:
            if index == count:       # delete the node 
                data = current.data
                self.delete_node_on_data( data )
                return

            else:                # move forward to the next node
                count += 1
                current  = current.next

        if count < index:
            print( "The list has too few nodes for this deletion." )   

#################################################################################
    def clear( self ):
        # Routine to clear (delete) the entire list
        self.tail     = None
        self.head     = None
        self.previous = None
        self.size     = 0
      