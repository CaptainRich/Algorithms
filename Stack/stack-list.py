""" An illustration of the "stack" data structure using a linked list."""
#################################################################################

import st_class

#################################################################################

# Define the stack, then test the push, pop, and peek operations.

food = st_class.Stack()

food.push( 'eggs' )
food.push( 'ham' )
food.push( 'bacon' )
food.push( 'cheese' )

print( '\nThe initial stack is:' )
food.print_st()            # print the contents of the stack

# Pop two elements off of the stack.
food.pop()
food.pop()
print( '\nAfter two pops, the stack is:' )
food.print_st()

# Test the "peek" operation which should return "ham", as the top of stack.
value = food.peek()
print( '\nPeeking at the top of stack yields: ', value )


# Pop the remaining two elements from the stack, then attempt a third pop.
food.pop()
food.pop()
print( '\nAfter two more pops:' )
food.print_st()

# Now attempt to "peek" at the empty stack.
value = food.peek()
print( '\nPeeking at the top of an empty stack yields: ', value )

