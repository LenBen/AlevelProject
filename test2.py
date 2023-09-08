import sounddevice as sd
from scipy.io.wavfile import write

fs = 44100 #sample rate
seconds = 3 #length

myrecording = sd.rec(int(seconds* fs), samplerate=fs, channels=2)
sd.wait()
write("Output.wav", fs, myrecording)