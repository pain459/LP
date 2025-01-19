from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
time = 0  # Start time
channel = 0
volume = 80  # Moderate volume
tempo = 60  # Beats per minute

midi.addTrackName(track, time, "Piano")
midi.addTempo(track, time, tempo)

# Define a peaceful piano melody
melody = [
    (60, 1), (62, 1), (64, 1), (67, 2),  # C, D, E, G
    (67, 1), (64, 1), (62, 1), (60, 2),  # G, E, D, C
    (64, 1), (67, 1), (69, 1), (71, 2),  # E, G, A, B
    (71, 1), (69, 1), (67, 1), (64, 2),  # B, A, G, E
]

# Add notes to the MIDI file
for note, duration in melody:
    midi.addNote(track, channel, note, time, duration, volume)
    time += duration

# Save the MIDI file
with open("piano_melody.mid", "wb") as midi_file:
    midi.writeFile(midi_file)
