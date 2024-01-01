import librosa, librosa.display
import matplotlib.pyplot as plot
import numpy as np

from RecordAndPlay import Audio
from CreateRhythm import CreateRhythm

audio = Audio()
cr = CreateRhythm()

class getDifference:
    def __init__(self) ->  None:
        self.score = 0
        self.sampleRate = audio.getSampleRate()
        # self.callFuncs()
    
    def callFuncs(self):
        cr.GetMusic()
        cr.calculateBarLength()
        # self.compareTimes()
        return None
    
    def _getAudioArray(self):
        audio, sampleRate = librosa.load("voice.wav")
        beatTimes = librosa.onset.onset_detect(y=audio, sr=self.sampleRate, units="time")
        return audio, beatTimes

    def plotGraph(self):
        audio, beatTimes = self._getAudioArray()
        modelArray, b = self.getModelTimes()
        plot.figure(figsize=(10,3))
        plot.ylim(-1,1)
        # librosa.display.waveshow(y=audio, sr=self.sampleRate)
        plot.vlines(beatTimes, -1, 1, colors="r")
        plot.vlines(modelArray, -1, 1, colors="g")
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
        if len(modelArray) != len(beatTimes):
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
        score = 0
        for i in range(len(value)):
            score += 1 / value[i]
        score *= 100
        score /= 4
        self.score = score
        return value

def main():

            
    # cr.GetMusic()
    # cr.calculateBarLength()
    # cr.calculateRecLength()

    getDiff = getDifference()
    getDiff.plotGraph()

    # getDiff.getModelTimes()
    getDiff.compareTimes()
    print(getDiff.score)


if __name__ =="__main__":
    main()
