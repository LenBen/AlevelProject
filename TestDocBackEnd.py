import pyaudio
import wave
import vlc

class Audio:
    def __init__(self):
        self.chunk = 512
        self.format = pyaudio.paInt16
        self.channels = 1
        self.rate = 44100
        self.record_time = 5
        self.output_filename = "voice.wav"
    
    def record(self, *args): # records for specified time
     
     p = pyaudio.PyAudio()
     stream = p.open(rate=self.rate,
                format=self.format,
                channels=self.channels,
                input=True,
                frames_per_buffer=self.chunk)
     frames = []

     print("recording start **")

     for i in range(0, int(self.rate / self.chunk * self.record_time)):
        data = stream.read(self.chunk)
        frames.append(data)

     print("** recording ended")

     stream.stop_stream()
     stream.close()
     p.terminate()

     wf = wave.open(self.output_filename, 'wb')
     wf.setnchannels(self.channels)
     wf.setsampwidth(p.get_sample_size(self.format))
     wf.setframerate(self.rate)
     wf.writeframes(b''.join(frames))
     wf.close()
    
    def PlayMusic(*args): # plays back the recording
        wav = vlc.MediaPlayer("voice.wav")
        wav.play()
    
    def setRecordTime(self, record_time: float) -> bool: # setter of record_audio

        try:   
            record_time = float(record_time)
        except:
            return False

        if record_time >= 0 and record_time <=60: # ensure the length of the string isn't negative or over 60s
            self.record_audio = record_time
            return True 
        else:
            return False
   
    def getRecordTime(self) -> int: # getter of record_audio
        return self.record_audio
    
    def getSampleRate(self) -> int:
        return self.rate