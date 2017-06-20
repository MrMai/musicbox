# single octave with sharps
o1_s = ['C', 'C♯', 'D', 'D♯', 'E', 'F', 'F♯', 'G', 'G♯', 'A', 'A♯', 'B']
# single octave with flats
o1_f = ['C', 'D♭', 'D', 'E♭', 'E', 'F', 'G♭', 'G', 'A♭', 'A', 'B♭', 'B']
# double octave with sharps
o2_s = o1_s * 2
# double octave with flats
o2_f = o1_f * 2

def sum_semi(a): # sums semitones behind each step in array, returns array (ex. [2, 1, 2] -> [2, 3, 5])
    b = [] # return array
    for d in range(0, len(a)):
        c = 0
        for e in range(0, d):
            c += a[e]
        b.append(c)
    return b

def note_shift(a, semi): # shifts array over by a determined amount of semitones, returns array (ex. 3semi [2, 3, 5] -> [5, 6, 8])
    b = a # return array
    for c in range(0, len(a)):
        b[c] += semi
    return b

def semi_to_note(a, sorf): # returns array of corrospoding string notes from semitone skips. sorf being true means it will be printed with sharps, false with flats
    d = [] # octave storage
    if(sorf == True):
        d = o2_s
    else:
        d = o2_f
    b = [] # return array
    for c in range(0, len(a)):
        b.append(d[a[c]])
    return b

def scan_for_item(a, item): # scans for item inside array a
    for b in range(0, len(a)):
        if(a[b] == item):
            return True
    return False

def scan_for_array_items(a, items): # scans for mutiple items in array
    c = 0
    for b in range(0, len(items)):
        if(scan_for_item(a, items[b])):
            c += 1
    if(c == len(items)):
        return True
    else:
        return False

def normalize_24(a):
    b = a
    for c in range(0, len(a)):
        if(a[c] < 12):
            if(scan_for_item(a, a[c] + 12) == False):
                b.append(a[c] + 12)
        if(a[c] > 11):
            if(scan_for_item(a, a[c] - 12) == False):
                b.append(a[c] - 12)
    return b

def gen_piano_keys24(a): # prints a ascii piano with keypresses from input array which should be given in numbered semitones (24 keys)
    blank = [' '] * 24
    asciipiano = """
    |  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
    |  |{1}| |{3}|  |  |{6}| |{8}| |{10}|  |  |{13}| |{15}|  |  |{18}| |{20}| |{22}|  |
    |  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
    | {0} | {2} | {4} | {5} | {7} | {9} | {11} | {12} | {14} | {16} | {17} | {19} | {21} | {23} |
    |___|___|___|___|___|___|___|___|___|___|___|___|___|___|
    """
    for b in range(0, len(a)):
        blank[a[b]] = '◍'
    asciipiano = asciipiano.format(*blank)
    return asciipiano

def sort_order(a, length): # returns an array of the sorted input array
    c = []
    for b in range(0, length):
        if(scan_for_item(a, b)):
            c.append(b)
    return c

def gen_piano_keys12(a): # prints a ascii piano with keypresses from input array which should be given in numbered semitones (12 keys)
    blank = [' '] * 12
    asciipiano = """
    |  | | | |  |  | | | | | |  |
    |  |{1}| |{3}|  |  |{6}| |{8}| |{10}|  |
    |  |_| |_|  |  |_| |_| |_|  |
    | {0} | {2} | {4} | {5} | {7} | {9} | {11} |
    |___|___|___|___|___|___|___|
    """
    for b in range(0, len(a)):
        if(a[b] < 12):
            blank[a[b]] = '◍'
    asciipiano = asciipiano.format(*blank)
    return asciipiano

def gen_ukulele_frets(a): # prints an ascii ukulele with the frets from input array which should be given in numbered semitones
    blank = [' '] * 24
    asciiuke = """
    ----+-------+-------+-------+-------+-------+-------+-------+-------+
     {9} A|   {10}   |   {11}   |   {12}   |   {13}   |   {14}   |   {15}   |   {16}   |   {17}   |
    ----+-------+-------+-------+-------+-------+-------+-------+-------+
     {4} E|   {5}   |   {6}   |   {7}   |   {8}   |   {9}   |   {10}   |   {11}   |   {12}   |
    ----+-------+-------+-------+-------+-------+-------+-------+-------+
     {0} C|   {1}   |   {2}   |   {3}   |   {4}   |   {5}   |   {6}   |   {7}   |   {8}   |
    ----+-------+-------+-------+-------+-------+-------+-------+-------+
     {7} G|   {8}   |   {9}   |   {10}   |   {11}   |   {12}   |   {13}   |   {14}   |   {15}   |
    ----+-------+-------+-------+-------+-------+-------+-------+-------+
    """
    for b in range(0, len(a)):
        blank[a[b]] = '◍'
    asciiuke = asciiuke.format(*blank)
    return asciiuke

def split(a): # returns a split array
    del a[int(len(a)/2):]
    return a



'''
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  | | | |  |  | | | | | |  |  | | | |  |  | | | | | |  |
|  |_| |_|  |  |_| |_| |_|  |  |_| |_|  |  |_| |_| |_|  |
|   |   |   |   |   |   |   |   |   |   |   |   |   |   |
|___|___|___|___|___|___|___|___|___|___|___|___|___|___|

◍
|  |C| |D|  |  |F| |G| |A|  |
|  |♯| |♯|  |  |♯| |♯| |♯|  |
|  |_| |_|  |  |_| |_| |_|  |
| C | D | E | F | G | A | B |
|___|___|___|___|___|___|___|


----+-------+-------+-------+-------+-------+-------+-------+-------+
   A|       |       |       |       |       |       |       |       |
----+-------+-------+-------+-------+-------+-------+-------+-------+
   E|       |       |       |       |       |       |       |       |
----+-------+-------+-------+-------+-------+-------+-------+-------+
   C|       |       |       |       |       |       |       |       |
----+-------+-------+-------+-------+-------+-------+-------+-------+
   G|       |       |       |       |       |       |       |       |
----+-------+-------+-------+-------+-------+-------+-------+-------+

----+-------+-------+-------+-------+-------+-------+-------+-------+
 {9} A|   {10}   |   {11}   |   {12}   |   {13}   |   {14}   |   {15}   |   {16}   |   {17}   |
----+-------+-------+-------+-------+-------+-------+-------+-------+
 {4} E|   {5}   |   {6}   |   {7}   |   {8}   |   {9}   |   {10}   |   {11}   |   {12}   |
----+-------+-------+-------+-------+-------+-------+-------+-------+
 {0} C|   {1}   |   {2}   |   {3}   |   {4}   |   {5}   |   {6}   |   {7}   |   {8}   |
----+-------+-------+-------+-------+-------+-------+-------+-------+
 {7} G|   {8}   |   {9}   |   {10}   |   {11}   |   {12}   |   {13}   |   {14}   |   {15}   |
----+-------+-------+-------+-------+-------+-------+-------+-------+


'''
