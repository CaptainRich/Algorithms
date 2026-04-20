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
    def append_at_a_location( self, data, index ):
        # Start at the 'head' and traverse to 'index', then insert/append.
        current  = self.head
        previous = self.head

        # Encapsulate the new data into a node.
        node = Node( data )

        count = 1
        while current:
            if index == 1:       # append at the start of the list
                node.next = current
                self.head = node
                print( "Appending to the list start." )
                self.size += 1
                return

            elif index == count: # insertion point found
                node.next     = current
                previous.next = node
                self.size     += 1
                return
            
            else:                # move forward to the next node
                count += 1
                previous = current
                current  = current.next

        if count < index:
            print( "The list has too few nodes for this insertion." )

##################################################################################
    def list_size( self) :
        # Simply traverse the list and count the items.
        count = 0
        current = self.head

        while current:
            count +=1
            current = current.next

        return count

##################################################################################
    def search( self, data ):
        # Search the list for a specific data item.
        for node in self.iter( ):
            if data == node:
                return True
            
        return False

#################################################################################
    def delete_last_node( self ):
        # Routine to delete the last node of the list
        current  = self.head      # both pointers are set to the start of the list
        previous = self.head

        while current:
            if current.next == None:           # found the last node
                previous.next = current.next   # which is 'None'
                self.size -= 1                 # reduce the size count

            # If not at the end of the list, move both pointers forward
            previous = current
            current  = current.next


#################################################################################
    def delete_based_on_data( self, data ):
        # Routine to delete a node from the list that matches 'data'.
        current  = self.head      # both pointers are set to the start of the list
        previous = self.head

        while current:
            if current.data == data:             # found the desired node
                if current == self.head:
                    self.head = current.next     # delete the first node

                else:
                    previous.next = current.next # delete by skipping over

                self.size -= 1                   # reduce the count

                return
            
            # If not the desired node, move both pointers forward
            previous = current
            current  = current.next

#################################################################################
    def clear( self ):
        # Routine to clear (delete) the entire list
        self.tail = None
        self.head = None
        self.size = 0
      