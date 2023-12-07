import muspy

# evaluate the music based on PR, NPC, POLY

# PR: Pitch Range
# NPC: Number of Pitch Classes
# POLY: Polyphony
file = muspy.read_midi('/workspaces/EMOPIA/gan_final.mid')
print( "the pitch range is: ", muspy.pitch_range(file))
print( "the number of pitch classes is: ", muspy.n_pitches_used(file))
print( "the polyphony is: ", muspy.polyphony(file))