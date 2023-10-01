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
   
   def setRecordTime(self, record_time) -> int:
      global record_audio
      nums = []
      rec_time = ""

      for n in range(len(record_time)):
         nums.append(record_time[n])

      try:
         for n in range(len(nums)):
            if (ord(nums[n]) <= 48 or ord(nums[n]) >= 57):
               return 55
      except:
         print("Error with ASCII")
         return 55
      
      for i in range(len(nums)):
         rec_time += str(nums[i])
      
      record_time = int(rec_time)
         
      record_time = int(record_time)

      if record_time >= 0 and record_time <=60:
         record_audio = record_time
         return 0 
      else:
         return 404
   
   def getRecordTime(self) -> int:
      global record_audio
      return record_audio

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

     #print(frames)

   def PlayMusic(*args, **kwargs):
        wav = vlc.MediaPlayer("voice.wav")
        wav.play()