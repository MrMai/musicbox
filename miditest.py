import midi, time

conn = midi.MidiConnector('/dev/ttyS0')
channel = 1
note = 40
topvelocity = 80

def notetrigger(notenumber, velocity, channel):
    notecommand = midi.NoteOn(notenumber, velocity)
    message = midi.Message(notecommand, channel)
    print(message)
    return message

while True:
    conn.write(notetrigger(note, topvelocity, channel))
    time.sleep(0.1)
    conn.write(notetrigger(note, 0, channel))
    time.sleep(1)
