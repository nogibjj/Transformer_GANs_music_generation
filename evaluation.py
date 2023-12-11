import muspy

# evaluate the music based on PR, NPC, POLY

# PR: Pitch Range
# NPC: Number of Pitch Classes
# POLY: Polyphony
file = muspy.read_midi('
print( "the pitch range is: ", muspy.pitch_range(file))
print( "the number of pitch classes is: ", muspy.n_pitches_used(file))
print( "the polyphony is: ", muspy.polyphony(file))

def evaluate(file):
    return muspy.pitch_range(file), muspy.n_pitches_used(file), muspy.polyphony(file)

def average_evalutation(file):
    len = len(evaluate(file))
    return sum(evaluate(file))/len