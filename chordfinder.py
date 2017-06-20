import semishort, semicore
#   semitone conpositions
# scales
maj_s     = [2,2,1,2,2,2,1] # major
nat_min_s = [2,1,2,2,1,2,2] # natural minor
har_min_s = [2,1,2,2,1,3,1] # harmonic minor
mel_min_s = [2,1,2,2,2,2,1] # melodic minor

# chords
maj7_c = [0,4,7,11] # major seventh
min7_c = [0,4,7,10] # minor seventh
maj_c  = [0,4,7]    # major

s = semicore.note_shift(maj7_c, 2)
print(semicore.semi_to_note(s, True))
print(semicore.gen_ukulele_frets(s))
