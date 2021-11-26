from pyRealParser import Tune
import re
import random
import numpy as np

sourcepath = '/Volumes/NAUTILUS/ML/MusicVAE/ChordHMM/jazz1350.txt'
with open(sourcepath) as f:
    url = f.read()
fullparse= Tune.parse_ireal_url(url);

songlist = []
for i in range(len(fullparse)):
    songlist.append(fullparse[i].measures_as_strings)


def cleanup(song_m):
    notes = 'A','Ab','A#','B','Bb','B#','C','Cb','C#','D','Db','D#','E','Eb','E#','F','Fb','F#','G','Gb','G#'
    regexPattern = '('+'|'.join(map(re.escape, notes))+')'
    cleaned_m = []

    for i in range(len(song_m)):
        x = re.split(regexPattern,song_m[i])
        y = []
        if '' in x:
            x.remove('')
            for k in range(0,len(x),2):
                y.append(x[k]+x[k+1])
                cleaned_m.append(y)

    for j in range(len(cleaned_m)):
        thism = cleaned_m[j]
        for k in range(len(thism)-2,-1,-1):
            if thism[k].endswith('/'):
                thism[k] = thism[k] + thism.pop(k+1)
    flat_m = [item for sublist in cleaned_m for item in sublist]
    return cleaned_m, flat_m

test = songlist[random.randrange(0,len(songlist))]
test_clean, test_flat = cleanup(test)
#print(test_clean,'\n\n',test_flat)

flattened_songs = []
cleaned_songs = []
for i in range(len(songlist)):
    song = songlist[i]
    clean, flat = cleanup(song)
    cleaned_songs.append(clean)
    flattened_songs.append(flat)

#print(flattened_songs)
