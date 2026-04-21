""" The main program/driver for the single linked list. """


import basics

####################################################################################################
####################################################################################################

# Function to print the current state of the list

def print_list( ):
    # Traverse the list and output the data.
    current = food.head
    while current:
        print( 'The nodes data is: ', current.data )
        current = current.next      # move to the next node if it exists.

    print( ' ' )


####################################################################################################
# Create sample nodes for the linked list.  Begin by defining the primary data.

food = basics.DoublyLinkedList()

food.append( 'eggs' )
food.append( 'ham' )
food.append( 'spam' )
print( ' ' )
print( 'The initial list.' )
print( 'The list size is: ', food.size, '\n' )
print_list()


# Test the 'append_at_start' function.
food.append_at_start( 'bacon' )
print( 'The list after appending "bacon" at the start of the list.' )
print( 'The list size is: ', food.size, '\n' )
print_list()

# Insert a new node with data that matches an existing node
food.append_at_a_location( 'ham' )
print( 'The list after inserting "ham" at the location of existing "ham". ' )
print( 'The list size is: ', food.size, '\n' )
print_list()


# Test the 'search' function.
print( ' ' )
print( 'Is "cheese" in the list?', food.search( 'cheese' ) )
print( 'Is "ham" in the list?', food.search( 'ham' ) )


# Now delete 'ham', based on the value of the node (ham).
food.delete_node_on_data( 'ham' )
print( '\nAfter deleting "ham" based on its value, the list is: ' )
print_list()
print( 'The current list size is: ', food.size, '\n' )

# Delete the 2nd occurrence of 'ham' based on its location index.
food.delete_node_on_location( 3 )
print( '\nAfter deleting "ham" based on its index (3)' )
print_list()
print( 'The current list size is: ', food.size, '\n' )

# Test deleting an index past the end of the list, which has 3 nodes now.
food.delete_node_on_location( 10 )
print( '\nAfter deleting a location past the end of the list.' )
print_list()
print( 'The current list size is: ', food.size, '\n' )

# Delete (clear) the entire list
food.clear()
print( 'After clearing the list, its size is: ', food.size )
print( 'Is "eggs" in the list?', food.search( 'eggs' ) )
