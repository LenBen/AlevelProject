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

    def getModelTimes(self):
        audio, beatTimes = self._getAudioArray()
        lengths = cr.calculateTimeOfNotes()
        modelArray = []
        modelArray.append(beatTimes[0]) # This gets rid of any error with the break at the beggining of the recording
        for i in range(len(lengths)):
            if i == 1:
                pass
            else:
                modelArray.append(modelArray[i - 1] + lengths[i])
        beatTimes = beatTimes.tolist()
        print("Lists")
        print(modelArray)
        print(beatTimes)
        return modelArray, beatTimes

    def compareTimes(self):
        modelArray, beatTimes = self.getModelTimes()
        if not(len(modelArray) == len(beatTimes)):
            raise(RuntimeError)
        value = []
        for i in range(len(modelArray)):
            if(beatTimes[i] <= modelArray[i] + 0.055) and (beatTimes[i] >= modelArray[i] - 0.055):
                value.append(1)
            elif(beatTimes[i] <= modelArray[i] + 0.085) and (beatTimes[i] >= modelArray[i] - 0.085):
                value.append(2)
            elif(beatTimes[i] <= modelArray[i] + 0.115) and (beatTimes[i] >= modelArray[i] - 0.115):
                value.append(3)
            elif(beatTimes[i] <= modelArray[i] + 0.145) and (beatTimes[i] >= modelArray[i] - 0.145):
                value.append(4)
            else:
                value.append(5)
        print(value)

    # def getDifference(self):
    #     audio, beatTimes = self._getAudioArray()
    #     beatTimes.tolist()
    #     for i in range(len(beatTimes)-1):
    #         self.timeDiffs.append(beatTimes[i+1] - beatTimes[i])
    #     print(self.timeDiffs)
    #     cr.GetMusic()
    #     cr._calculateBeatLength()
    #     length = []
    #     for i in range(len(self.timeDiffs)):
    #         length.append(self.timeDiffs[i] * cr.beatLength)
    #     self.timeDiffs = length

    # def compareTimes(self):
    #     modelRhythm = cr.calculateDiffs()
    #     if not(len(modelRhythm) and len(self.timeDiffs)):
    #         raise(RuntimeError)
    #     value = []
    #     for i in range(len(modelRhythm)):
    #         if (self.timeDiffs[i] >= modelRhythm[i] + 0.3) and (self.timeDiffs[i] <= modelRhythm[i] -0.3):
    #             value.append(1)
    #         elif (self.timeDiffs[i] >= modelRhythm[i] + 0.5) and (self.timeDiffs[i] <= modelRhythm[i] - 0.5):
    #             value.append(2)
    #         elif (self.timeDiffs[i] >= modelRhythm[i] + 0.8) and (self.timeDiffs[i] <= modelRhythm[i] - 0.8):
    #             value.append(3)
    #     return value


    
            
cr.GetMusic()
cr.calculateBarLength()
# cr.calculateRecLength()


getDiff = getDifference()
# getDiff.getDifference()
# getDiff.plotGraph()

getDiff.getModelTimes()
getDiff.compareTimes()
