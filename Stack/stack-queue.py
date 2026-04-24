""" An illustration of the "stack" data structure using a queue structure."""
#################################################################################

import q_class

#################################################################################

# Define the stack, then test the push, pop, and peek operations.

q = q_class.ListQueue()

q.enqueue( 20 )
q.enqueue( 30 )
q.enqueue( 40 )
q.enqueue( 50 )            # Note this item exceeds the size of the queue

print( '\nThe items in the queue are:' )
print( q.items )

# Remove items from the queue, first in is first out.
data = q.dequeue()
print( '\nThe first item dequeued is:', data )
print( 'The queue is: ', q.items )
data = q.dequeue()
print( '\nThe second item dequeued is:', data )
print( 'The queue is: ', q.items )
data = q.dequeue()
print( '\nThe third item dequeued is:', data )
print( 'The queue is: ', q.items )
data = q.dequeue()
print( '\nThe fourth item dequeued is:', data )
print( 'The queue is: ', q.items )

