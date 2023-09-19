import pyaudio
import wave
import vlc

CHUNK = 512
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
record_audio = 5
WAVE_OUTPUT_FILENAME = "voice.wav"

class Audio:
    def __init__(self) -> None:
       pass

    def record(*args, **kwargs):
     
     p = pyaudio.PyAudio()
     stream = p.open(rate=RATE,
                format=FORMAT,
                channels=CHANNELS,
                input=True,
                frames_per_buffer=CHUNK)
     frames = []

     print("recording start **")

     for i in range(0, int(RATE / CHUNK * record_audio)):
        data = stream.read(CHUNK)
        frames.append(data)

     print("** recording ended")

     stream.stop_stream()
     stream.close()
     p.terminate()

     wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
     wf.setnchannels(CHANNELS)
     wf.setsampwidth(p.get_sample_size(FORMAT))
     wf.setframerate(RATE)
     wf.writeframes(b''.join(frames))
     wf.close()

    def PlayMusic(*args, **kwargs):
        wav = vlc.MediaPlayer("voice.wav")
        wav.play()