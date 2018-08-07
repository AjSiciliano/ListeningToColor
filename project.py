import math
import skimage
import numpy as np
from skimage import data
import multiprocessing as MP
import pretty_midi
import librosa

incrementation = 0.44
name = "yellwish"
tag = ".jpg"
img = data.load(name + tag)
octiveIncremenation = 0
track = pretty_midi.PrettyMIDI(initial_tempo=80)
instrument = pretty_midi.Instrument(program=24, is_drum=False, name='Piano YUH')

#red (R),blue (B),green (G),yellow (Y),purple(P),black(L),white(W),grey(E),orange(O),dark,light
CLRS = [0,0,0,0,0,0,0,0,0,0,0]
CHORDS = []

def sorter(LIST):
    #BUBBLE SORT
    def swap(index1,index2):
        i = LIST[index1]
        LIST[index1] = LIST[index2]
        LIST[index2] = i
          
    for x in range(0,len(LIST)-1,1):
        for y in range(len(LIST)):
            if float(LIST[y][1:]) > float(LIST[x + 1][1:]):
                swap(x + 1,y)
    return LIST
            

def colorFy(p):
    index = maximize(p)
    if (p[0] < 30) and (p[1] < 30) and (p[2] < 30):
        return 5 #black
    elif (p[0] > 250) and (p[1] > 250) and (p[2] > 250):
        return 6 #white
    elif (p[1] < 130) and (p[0] >= 160) and (p[2] >= 160) and (p[2] >= p[0]):
        return 4 #purple
    elif (p[0] >= 200) and (p[2] <= 80) and p[1] < 190 and p[1] > 100:
        return 8 #orange
    elif (p[2] < 120) and (p[1] >= 215) and (p[0] >= 215) and (p[0] >= p[1]):
        return 3  #yellow
    elif (
        (
            ((p[0] >= p[index]) and (p[0] <= p[index] + 14)) and
            ((p[1] >= p[index]) and (p[1] <= p[index] + 14)) and
            ((p[2] >= p[index]) and (p[2] <= p[index] + 14))
        )
           or
        (
            ((p[0] <= p[index]) and (p[0] >= p[index] - 14)) and
            ((p[1] <= p[index]) and (p[1] >= p[index] - 14)) and
            ((p[2] <= p[index]) and (p[2] >= p[index] - 14))
        )
    ): 
        return 7 #grey
    else:
        if index == 0:
            return 0 #red
        if index == 1:
            return 2 #green
        if index == 2:
            return 1 #blue
    
def exposure(p):
    total = 0
    for x in p:
        total += x
    if ((total / len(p)) < 130):
        return 9 #dark
    else:
        return 10 #light
def splitter(initial, splits):
    
    def firstHalf(array):
        halfpoint = math.trunc(len(array) / 2)
        return array[:halfpoint]
    def secHalf(array):
        halfpoint = math.trunc(len(array) / 2)
        return array[halfpoint:]
    
    buffer = [initial]

    for x in range(splits):
        g = [] 
        for index in range(len(buffer)):
            g.append(firstHalf(buffer[index]))
            g.append(secHalf(buffer[index]))
        buffer[:]
        buffer = g
    return buffer

def total(array):
    t = 0
    for x in array:
        t += x
    return t

def maximize(array):
    index = 0
    for x in range(0, len(array)):
        if array[x] >= array[index]:
            index = x
    return index

def colorCoder (array , Q):
    #rgb
    #red,blue,green,yellow,purple,black,white,grey,orange,dark,light
    colors = [0,0,0,0,0,0,0,0,0,0,0]
    for row in array:
        for p in list(row):
            colors[(colorFy(p))] += 1
            colors[(exposure(p))] += 1
    print(colors)
    Q.put(colors)
        
def Analy():
    col = []
    s = splitter(list(img), math.trunc(math.log(64, 2)))
    q = MP.Queue()
    processes = []
    if __name__ == '__main__':
        for x in s:
            p = MP.Process(target=colorCoder, args=(x,q))
            processes.append(p)
            print("PROCESS APPENDED")
            p.start()

        for x in range(MP.cpu_count()):
            col.append(q.get())
        
        for x in processes:
            x.join()
        q.close()
        q.join_thread()
        
    for x in col:
        # x is the indiviual color-makeup for each quadrant
        for y in range(len(x)):
            CLRS[y] += x[y] 

    

def chordify(color):
    
    if color == 'R':
        print("C^(6 9) --> RED CHORD")
        n = [45,52,55,60,62,67]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                n[x] += 12
            octiveIncrementation -= 1
        
        
        return n
    elif color == 'B':
        print("D^(6) --> BLUE CHORD")
        n = [47,54,57,52,66]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
            
        
        return n
    elif color == 'G':
        n = [48,55,59,64]
        print("C^(Maj 7) --> GREEN CHORD")
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'Y':
        print("G^(6) --> YELLOW CHORD")
        n = [52,59,62,67]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'P':
        print("G^(Maj 7 9) --> PURPLE CHORD")
        n = [43,50,57,59,62,66]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'L':
        print("F#^(7) --> BLACK CHORD")
        n = [42,49,52,58,62]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'W':
        print("E-^(7 9 11) --> WHITE CHORD")
        n = [40,47,54,55,62,66,69]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'E':
        print("G+^(Maj 7) --> GREY CHORD")
        n = [47,54,59,63,67]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    elif color == 'O':
        print("G^(Maj 7) --> ORANGE CHORD")
        n = [50,54,62,67]
        
        while octiveIncremenation != 0:
            for x in range(len(n)):
                if octiveIncremenation < 0:
                    n[x] -= 12
                else:
                    n[x] += 12
            if octiveIncremenation < 0:
                octiveIncrementation += 1
            else:
                octiveIncrementation -= 1
        
        
        return n
    
def zeroes(LIST):
    t = 0
    for x in LIST:
        if math.trunc(float(x[1:])) == 0:
            t += 1
    return t
 
def writer(): 
    def indexer(index):
        if index == 0:
            return 'R'
        elif index == 1:
            return 'B'
        elif index == 2:
            return 'G'
        elif index == 3:
            return 'Y'
        elif index == 4:
            return 'P'
        elif index == 5:
            return 'L'
        elif index == 6:
            return 'W'
        elif index == 7:
            return 'E'
        elif index == 8:
            return 'O'
    
    
    colorscoded = []
    t = total(CLRS[:9])
    print(CLRS)
    for x in range(len(CLRS) - 2):
        n = (CLRS[x] / t) * 100
        if n < 1:
            n *= 10
        num = str(math.trunc(n))
        colorscoded.append(indexer(x) + num)
                  
    s = sorter(colorscoded)
    z = zeroes(s)
    
    while z < 8:
        for x in range(len(s)):
            if s[x][1:] != '0':
                CHORDS.append(s[x][:1])
                s[x] = s[x][:1] + str(int(s[x][1:]) - 1)
        z = zeroes(s)
    
    for x in range(0,int(s[8][1:]), 5):
        CHORDS.append(s[8][:1])
    
    def swap(index1,index2):
        i = CHORDS[index1]
        CHORDS[index1] = CHORDS[index2]
        CHORDS[index2] = i
    
    for x in range(0, 12, 1):
        for x in range(int(math.trunc(len(CHORDS) / 2)),len(CHORDS),1):
            for y in range(0, len(CHORDS), 2):
                swap(x, y)
        for x in range(len(CHORDS) - 1,int(math.trunc(len(CHORDS) / 2)),-2):
            for y in range(0, len(CHORDS), 1):
                swap(x, y)
        

        
def maker():
    elapsed = incrementation
    
    for x in CHORDS:
        for y in chordify(x):
            note = pretty_midi.Note(100, y, elapsed - incrementation, elapsed)
            instrument.notes.append(note)
        elapsed += incrementation
    
    track.instruments.append(instrument)
    audio_out = track.synthesize(fs=16000)
    track.write(name + ".mid")
    librosa.output.write_wav(name + ".wav",audio_out,sr = 16000)


def mixr():
    global incrementation
    t = CLRS[10] + CLRS[9]
    LIGHT = 100 * (CLRS [9] / t)
    
    if LIGHT <= 50:
        print("DOWN AN OCTIVE")
        octiveIncremenation = -1
        incrementation = 1.25
    elif LIGHT > 70 and LIGHT <= 80:
        print("UP AN OCTIVE")
        incrementation = 1
        octiveIncrementation = 0.75
    elif LIGHT > 80 and LIGHT <= 85:
        print("UP TWO OCTIVES")
        incrementation = 0.5
        octiveIncrementation = 2
    elif LIGHT >= 90:
        incrementation = 0.2
        octiveIncrementation = 3
    else:
        print("NO OCTIVE INCREMENTATION")
    
    if(LIGHT >= 50 and LIGHT < 75):
        instrument.program = 73
    
    
Analy()    
writer()
mixr()
maker()








