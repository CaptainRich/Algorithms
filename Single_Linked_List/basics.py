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

##################################################################################
    def iter( self ):
        # This function is a 'generator' saving its state between calls.
        current = self.head
        
        while current:
            val = current.data
            current = current.next  # move on to the next item in the list
            yield val


##################################################################################
    def append( self, data ):
        # Encapsulate the data in a Node.
        node = Node( data )
        if self.tail:             # add at the end of the list
            self.tail.next = node # update the current node to point to the new node
            self.tail = node      # set the tail to the new node

        else:                     # the first entry in an empty list
            self.head = node
            self.tail = node

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
      