import pyaudio
import wave

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
record_audio = 5
WAVE_OUTPUT_FILENAME = "voice.wav"

p = pyaudio.PyAudio()

stream = p.open(rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=True,
                frames_per_buffer=CHUNK)

print("THis is the record thing, please enter the amount of seconds you want to record")
record_audio: int = int(input())

print("* recording")

frames = []

for i in range(0, int(RATE / CHUNK * record_audio)):
    data = stream.read(CHUNK)
    frames.append(data)

print("* done recording")

stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()