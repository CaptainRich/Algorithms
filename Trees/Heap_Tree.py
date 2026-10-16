""" An illustration of a Heap, implemented with a tree structure."""
#################################################################################
"""The heap is a tree structure setup such that a parent node at index 'i' has a 
   left child at index '2i' and a right child at index '2i+1'. Similarly, if a
   node has an index of '4', its parent is at index '4/2 or 2'.  Integer division
   is used to truncate the remainder when odd numbered indexes are divided by 2."""


################################################################################

# Define the class and methods for the tree structure.

################################################################################
class MinHeap:
    # A Min Heap is structured so that a parent node is less than or equal to
    # its children node(s).

    def __init__(self):
        self.heap = [0]    # this is a dummy element to facilitate indexing with
                           # integer division
        self.size = 0

    ############################################################################
    def arrange( self, i ):
        # A helper function to rearrange the heap as necessary, based on the index "i".

        while i // 2> 0:      # until we reach past the root of the tree

            # If the current node is less than its parent, swap them
            if self.heap[i] < self.heap[i//2]:
                self.heap[i], self.heap[i//2] = self.heap[i//2], self.heap[i]

            i //= 2           # move up the tree

    ############################################################################
    def insert( self, newNode ):
        # A  function to insert a new node into the heap.

        self.heap.append( newNode )
        self.size += 1
        self.arrange( self.size )


    ############################################################################
    def minimum_child( self, i ):
        # A helper function to determine the smallest child of a node.

        if i*2+1 > self.size:
            return i * 2           # there is no right child

        elif self.heap[i*2] < self.heap[i*2+1]:
            return i * 2           # the left child is smaller

        else:
            return i * 2 + 1       # the right child is smaller


    ################################################################################
    def sink( self, i ):
        # A  function to rearrange the heap by percolating downward.

        while i*2 < self.size:
            mn_child = self.minimum_child(i)

            if self.heap[i] > self.heap[mn_child]:
                self.heap[i], self.heap[mn_child] = self.heap[mn_child], self.heap[i]

            i = mn_child           # set the new index to the old child


    ################################################################################
    def delete_the_root( self ):
        # A function to delete the root node of a minHeap.

        item = self.heap[1]

        self.heap[1] = self.heap[self.size]     # set new root to the last node
        self.size -= 1                          # reduce the heap size
        self.heap.pop()                         # remove the root node
        self.sink( 1 )                          # reorder from the root index

        return item                             # return the old root


################################################################################

# Implement a heap and its functionality.

h = MinHeap()

for i in ( 4, 8, 7, 2, 9, 10, 5, 1, 3, 6 ):
    h.insert( i )

print( '\nPrinting the heap, output should be: 0,1,2,5,3,6,10,7,8,4,9')
print( h.heap )

# Create a new heap and test the deletion of the root node
h2 = MinHeap()

for i in ( 2, 3, 5, 7, 9, 10, 6 ):
    h2.insert( i )

print( '\nPrinting the new heap, out put should be: 0,2,3,5,7,9,10,6' )
print( h2.heap )

rnode = h2.delete_the_root()
print( '\nDeleting the root node: ', rnode )
print( '\nThe new heap should be: 0,3,6,5,7,9,10')
print( h2.heap )


        
