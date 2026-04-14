""" The main program/driver for the single linked list. """


import basics

####################################################################################################
####################################################################################################

# Create sample nodes for the linked list.  Begin by defining the primary data.

food = basics.SinglyLinkedList()

food.append( 'eggs' )
food.append( 'ham' )
food.append( 'spam' )

# Traverse the list and output the data.
current = food.head
while current:
    print( 'The nodes data is: ', current.data )
    current = current.next      # move to the next node if it exists.

