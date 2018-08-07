###import skimage
###from skimage import data, exposure
###from skimage.viewer import ImageViewer
###
###img = data.load("block.png")
##
##
###viewer = ImageViewer()
###viewer.show()
##
##import multiprocessing as MP
##
###import threading
###from threading import Thread
##
###def func1():  
###    print ('Working')
###    j += 10
###
###def func2():
###    print ('Working')
###
###if __name__ == '__main__':
###    
##    
##
##def y (i, q):
##    print("IT workedish")
##    q.put(i + 10)
##    q.put(i * 300)
##    
##    
###
###    
###
###
##
##def reader(queue):
##    l = []
##    for x in range(2):
##        l.append(queue.get())
##    return l
##    
##if __name__ == '__main__':
##    
###    pool = MP.Pool(process=4)
##    q = MP.Queue()
##
##    #    
##    proc = MP.Process(target=y, args=(1,q))
##    proc.start()
##    
##    print(reader(q))
##    
##    proc.join()
##    
##    q.close()
##    q.join_thread()
###    
##
##    
##    
###    proc2 = MP.Process(target=yuh, args=(2,q))
###    proc2.start()
###    proc2.join()
###    
###    print(q.get())
###    print(q2.get())
###   
###    q2.close()
###    q2.join_thread()
###
###
###[[1, 2], [3, 4, 5], [6, 7], [8, 9, 10]]
##
##
###def firstHalf(array):
###    halfpoint = math.trunc(len(array) / 2)
###    return array[:halfpoint]
###def secHalf(array):
###    halfpoint = math.trunc(len(array) / 2)
###    return array[halfpoint:]
###    
###def splitter(initial, splits):
###    buffer = [initial]
###
###    for x in range(splits):
###        g = [] 
###        for index in range(len(buffer)):
###            g.append(firstHalf(buffer[index]))
###            g.append(secHalf(buffer[index]))
###        buffer[:]
###        buffer = g
###    return 
###        
###    print(buffer)
###    
###splitter([1,2,3,4,5,6,7,8,9,10], 4)
##
###print(math.log(64, 2))
#import numpy as np
##def blockshaped(arr, nrows, ncols):
##    h = arr.shape[0]
##    h = arr.shape[1]
##    return (arr.reshape(h//nrows, nrows, -1, ncols)
##               .swapaxes(1,2)
##               .reshape(-1, nrows, ncols))
#
#
#array = np.array([
#    [1,2,3,4,5,6],
#    [7,8,9,10,11,12],
#    [12,13,14,15,16,17],
#    [18,19,20,21,22,23],
#    [24,25,26,27,28,29],
#    [30,31,32,33,34,35]])
#
#
#print(len(array))
#print(int(len(array) / 2))
#for x in blockshaped(array,int(len(array) / 2),int(len(array) / 2)):
#    print(1)
#
#
#
#
#import math
#import skimage

#from skimage import data
#import multiprocessing as MP
#img = data.load("Starry-Night.jpg")
#print(img.shape)
#
##j = (blockshaped(img,8,8))
#
##print(len(img))
#
##for x in j:
##    for y in x:
##        for f in y:
##            v = 0
#


#
#def sorter(LIST):
#    
#    def swap(index1,index2):
#        i = LIST[index1]
#        LIST[index1] = LIST[index2]
#        LIST[index2] = i
#        
#        
#    for x in range(0,len(LIST)-1,1):
#        for y in range(len(LIST)):
#            if LIST[y] > LIST[x + 1]:
#                swap(x + 1,y)
#                
#
#y = "HELLO"
#print(y[:3])
#                

import librosa
import numpy as np
import pretty_midi
import IPython.display

pm = pretty_midi.PrettyMIDI(initial_tempo=80)

inst = pretty_midi.Instrument(program=42, is_drum=False, name='my cello')

velocity = 100

for pitch, start, end in zip([60, 64, 67], [0.2, 0.6, 1.0], [1.1, 1.7, 2.3]):
    inst.notes.append(pretty_midi.Note(velocity, pitch, start, end))

'''
pitchlist = [60, 62, 64]
startlist = [0.2, 0.6, 1.0]
endlist = [1.1, 1.7, 2.3]
for i in range(3):
    inst.notes.append(pretty_midi.Note(velocity, pitchlist[i], startlist[i], endlist[i]))
'''

pm.instruments.append(inst)

#IPython.display.Audio(pm.synthesize(fs=16000), rate=16000)

#audio_out = pm.synthesize(fs=16000)
audio_out = pm.fluidsynth(fs=16000)
librosa.output.write_wav("foo.wav",audio_out,sr = 16000)










