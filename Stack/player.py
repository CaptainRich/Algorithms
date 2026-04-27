""" An illustration of the implementation of a queue data structure."""
#################################################################################

import media_player as mp

#################################################################################

# Define a few tracks for the media player to play.

track1 = mp.Track( "Sultans of Swing" )
track2 = mp.Track( "Clocks" )
track3 = mp.Track( "More Than A Feeling" )

# Dump out the tracks and their (random) lengths.
print( '\nThe tracks and their play time: ' )
print( track1.title, ' \t', track1.length )
print( track2.title, ' \t\t', track2.length )
print( track3.title, ' \t', track3.length )


# Now add the tracks to the media player
media_player = mp.MediaPlayerQueue()

media_player.add_track( track1 )
media_player.add_track( track2 )
media_player.add_track( track3 )

# Now play the tracks.
media_player.play()



