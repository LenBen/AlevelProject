import librosa, librosa.display
import matplotlib.pyplot as plot

from RecordAndPlay import Audio

audio = Audio()

# audio, sampleRate = librosa.load("voice.wav")
# beatTimes = librosa.onset.onset_detect(y=audio, sr=sampleRate, units="time")

# plot.figure(figsize=(10,3))
# plot.ylim(-1,1)
# librosa.display.waveshow(audio, sr=sampleRate)
# plot.vlines(beatTimes, -1, 1, colors="r")
# plot.show()

class getDifference:
    def __init__(self) ->  None:
        self.timeDiffs = []
        self.sampleRate = audio.getSampleRate()
    
    def getAudioArray(self):
        audio, sampleRate = librosa.load("voice.wav")
        beatTimes = librosa.onset.onset_detect(y=audio, sr=self.sampleRate, units="time")
        return audio, beatTimes

    def plotGraph(self):
        audio, beatTimes = self.getAudioArray()
        plot.figure(figsize=(10,3))
        plot.ylim(-1,1)
        librosa.display.waveshow(audio, sr=self.sampleRate)
        plot.vlines(beatTimes, -1, 1, colors="r")
        plot.show()

getDiff = getDifference()
getDiff.plotGraph()