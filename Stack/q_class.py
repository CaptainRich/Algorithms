""" Class definitions for stack operations using queues."""

""" Define the major queue classes and methods. """

#################################################################################
class ListQueue:
    def __init__(self):
        self.items = []                    # initially nothing in the queue
        self.front = self.rear = 0         # the queue is empty
        self.size  = 3                     # the maximum queue capacity

#################################################################################
    def enqueue( self, data ):
        # Adding items to a queue is "enqueuing".

        if self.size == self.rear:
            print( '\nThe queue is full.' )

        else:
            self.items.append( data )     # items are appended at the rear
            self.rear += 1


#################################################################################
    def dequeue( self ):
        # Removing the first item from a queue is "dequeuing".    

        if self.front == self.rear:
            print( '\nThe queue is empty.' )

        else:
            data = self.items.pop(0)   # deletes an item from the front of the queue
            self.rear -= 1             # adjust the rear pointer
            return data
        
