import librosa, librosa.display
import matplotlib.pyplot as plot

audio, sampRate = librosa.load("voice.wav")
# tempo, beatTimes = librosa.beat.beat_track(y=audio, sr=sampRate, start_bpm=60, units="time", tightness=0.001)
beatTimes = librosa.onset.onset_detect(y=audio, sr=sampRate, units="time")
print(beatTimes)

def graph():
    plot.figure(figsize=(10,3))
    plot.ylim(-1,1)
    librosa.display.waveshow(audio, sr=sampRate)
    plot.vlines(beatTimes, -1, 1, colors="r")
    plot.show()

print("Show graph? Y/N")
y = input()
if y == "Y":
    graph()
