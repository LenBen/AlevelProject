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
        print(beatTimes)
        plot.show()

    def getDifference(self):
        audio, beatTimes = self._getAudioArray()
        beatTimes.tolist()
        for i in range(len(beatTimes)-1):
            self.timeDiffs.append(beatTimes[i+1] - beatTimes[i])
        print(self.timeDiffs)
        cr.GetMusic()
        cr._calculateBeatLength()
        length = []
        for i in range(len(self.timeDiffs)):
            length.append(self.timeDiffs[i] * cr.beatLength)
        self.timeDiffs = length

    def compareTimes(self):
        modelRhythm = cr.calculateDiffs()
        if not(len(modelRhythm) and len(self.timeDiffs)):
            raise(RuntimeError)
        value = []
        for i in range(len(modelRhythm)):
            if (self.timeDiffs[i] >= modelRhythm[i] + 0.3) and (self.timeDiffs[i] <= modelRhythm[i] -0.3):
                value.append(1)
            elif (self.timeDiffs[i] >= modelRhythm[i] + 0.5) and (self.timeDiffs[i] <= modelRhythm[i] - 0.5):
                value.append(2)
            elif (self.timeDiffs[i] >= modelRhythm[i] + 0.8) and (self.timeDiffs[i] <= modelRhythm[i] - 0.8):
                value.append(3)


    
            

getDiff = getDifference()
# getDiff.getDifference()
getDiff.plotGraph()