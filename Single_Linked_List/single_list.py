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

food = basics.SinglyLinkedList()

food.append( 'eggs' )
food.append( 'ham' )
food.append( 'spam' )
print( ' ' )
print( 'The initial list.' )
print( 'The list size is: ', food.size )
print_list()




# Test the 'append_at_a_location' function.
food.append_at_a_location( 'bacon', 2 )
print( 'The list after appending "bacon" as the 2nd item.' )
print( 'The list size is: ', food.size )
print_list()


food.append_at_a_location( 'cheese', 1 )
print( 'The list after appending "cheese" to the beginning.' )
print( 'The list size is: ', food.size )
print_list()

food.append_at_a_location( 'tomatoes', 10 )   # past the end of the list
print( 'The list size is: ', food.size )
print_list()

print( 'The current list size is: ', food.list_size() )

# Test the 'search' function.
print( ' ' )
print( 'Is "cheese" in the list?', food.search( 'cheese' ) )
print( 'Is "tomatoes" in the list?', food.search( 'tomatoes' ) )

# Delete 'spam' from the list, which is the last node.
food.delete_last_node()
print( 'After deleting the last node (spam), the list is: ' )
print_list()
print( 'The current list size is: ', food.list_size() )
