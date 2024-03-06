import librosa, librosa.display
import matplotlib.pyplot as plot
import numpy

from RecordAndPlay import Audio
from CreateRhythm import CreateRhythm

audio = Audio()
cr = CreateRhythm()

class getDifference:
    def __init__(self) ->  None:
        self.score : int = 0
        self.sampleRate : int = audio.getSampleRate()
        self.audioArray : any = []
        self.modelArray : list = []
        self.scoreValues : list = []
    
    def _getAudioArray(self) -> None: # gets the Audio array
        audio, sr  = librosa.load("voice.wav")
        self.audioArray = librosa.onset.onset_detect(y=audio, sr=self.sampleRate, units="time") # Uses librosa to detect the beats of the audio file
        self.audioArray = numpy.array(self.audioArray)
        self.audioArray = self.audioArray.tolist()
        self._cleanUpAudioArray()

    def _cleanUpAudioArray(self) -> None: # Gets rid of beats within 0.1s
        for i in range(len(self.audioArray)):
            if self.audioArray[i] <= 0.1:
                self.audioArray = list(self.audioArray) # python didn't want to allow the remove function
                self.audioArray.remove(self.audioArray[i])

    def getModelTimes(self) -> None:

        self._getAudioArray()
        lengthArray = cr.getLengthArray()
        self.modelArray.append(self.audioArray[0]) # This alligns the model times and the audio array
        
        for i in range(len(lengthArray)): # This creates the model array
            if i == 0:
                pass # Skips the fist time, due to the earlier synchronisation
            else:
                self.modelArray.append(self.modelArray[i-1] + lengthArray[i-1]) # Adds time to beat before

    def plotGraph(self) -> None: # Plots the graph
        plot.figure(figsize=(10,3))
        plot.ylim(-1,1)
        plot.vlines(self.audioArray, -1, 1, colors="r") # user times in red
        plot.vlines(self.modelArray, -1, 1, colors="g") # model times in green
        plot.show()  

    def compareTimes(self) -> None:
        if self.modelArray == []: # Checks to make sure that the model array exists
            self.getModelTimes()

        if not( len(self.modelArray) == len(self.audioArray) ): # Checks that the lists are the same length
            self.score = -1
            return None
        
        for i in range(len(self.modelArray)): # compares the times and gives then a score.
            match (True):
                case _ if (self.audioArray[i] <= self.modelArray[i] + 0.055) and (self.audioArray[i] >= self.modelArray[i] - 0.055):
                    self.scoreValues.append(1)
                case _ if (self.audioArray[i] <= self.modelArray[i] + 0.055) and (self.audioArray[i] >= self.modelArray[i] - 0.055):
                    self.scoreValues.append(2)
                case _ if (self.audioArray[i] <= self.modelArray[i] + 0.055) and (self.audioArray[i] >= self.modelArray[i] - 0.055):
                    self.scoreValues.append(3)
                case _ if (self.audioArray[i] <= self.modelArray[i] + 0.055) and (self.audioArray[i] >= self.modelArray[i] - 0.055):
                    self.scoreValues.append(4)
                case _:
                    self.scoreValues.append(5)

        for i in range(len(self.scoreValues)): # calculates percentage score
            self.score += 1 / self.scoreValues[i]
        self.score = (self.score * 100) / len(self.scoreValues)


def main():
    cr.GetMusic()
    cr.calculateBeatLength()
    cr.calculateRecLength()

    gd = getDifference()
    gd.getModelTimes()
    print(gd.audioArray)
    print(cr.getLengthArray())
    print(gd.modelArray)
    # print(len(gd.modelArray))
    # print(len(gd.audioArray))
    gd.compareTimes()
    print(gd.scoreValues)
    if gd.score != -1:
        print(1)
    else:
        print(gd.score)

if __name__ == "__main__":
    main()