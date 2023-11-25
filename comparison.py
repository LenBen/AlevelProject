import librosa, librosa.display
import matplotlib.pyplot as plot
import numpy as np

from RecordAndPlay import Audio
from CreateRhythm import CreateRhythm

audio = Audio()
cr = CreateRhythm()

class getDifference:
    def __init__(self) ->  None:
        self.timeDiffs = []
        self.sampleRate = audio.getSampleRate()
    
    def _getAudioArray(self):
        audio, sampleRate = librosa.load("voice.wav")
        beatTimes = librosa.onset.onset_detect(y=audio, sr=self.sampleRate, units="time")
        return audio, beatTimes

    def plotGraph(self):
        audio, beatTimes = self._getAudioArray()
        plot.figure(figsize=(10,3))
        plot.ylim(-1,1)
        librosa.display.waveshow(y=audio, sr=self.sampleRate)
        plot.vlines(beatTimes, -1, 1, colors="r")
        plot.show()

    def getDifference(self):
        audio, beatTimes = self._getAudioArray()
        beatTimes.tolist()
        for i in range(len(beatTimes)-1):
            self.timeDiffs.append(beatTimes[i+1] - beatTimes[i])
        print(self.timeDiffs)
        cr.GetMusic()
        cr._calculateBeatLength()
        print(cr.beatLength)
        print(cr.lengthArray)
            

getDiff = getDifference()
getDiff.getDifference()