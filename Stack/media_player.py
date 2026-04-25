""" Class definitions for a sample media player, using queues."""

from random import randint
import time
import ql_class

class Track:
    """ This defines the (musical) track class. """
    def __init__( self, title=None ):
          self.title  = title
          self.length = randint( 5, 10 )   # fictitious track length


class MediaPlayerQueue( ql_class.Queue ):
     # The media player class, based on the queue class

     def add_track( self, track ):
          # Add a track to the play list
          self.ql_class.enqueue( track )


     def play( self ):
         # Play the next track from the queue

         while self.count > 0:
              current_track_node = self.ql_class.dequeue()
              print( '\nNow playing {}'.format( current_track_node.data.title) )
              time.sleep( current_track_node.data.length )

