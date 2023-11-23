import librosa, librosa.display
import matplotlib.pyplot as plot
import numpy 
import RecordAndPlay

audio, sampRate = librosa.load("download.wav")
tempo, beatTimes = librosa.beat.beat_track(y=audio, sr=sampRate, start_bpm=60, units="time")
print(tempo)
print(beatTimes)

# plot.figure(figsize=(14, 5))
# librosa.display.waveshow(y=audio, sr=sampRate)
# plot.vlines(beatTimes, -1, 1, color="r")
# plot.ylim(-1,1)
# fig, ax = plot.subplots(nrows=3, sharex=True)
# librosa.display.waveshow(audio, sr=sampRate, label="rhythm", ax=ax[2])
librosa.display.waveshow(beatTimes)