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
   
   def setRecordTime(self, record_time) -> bool: # setter of record_audio
      global record_audio
      nums = []
      rec_time = ""

      for n in range(len(record_time)): # turn the input into an array
         nums.append(record_time[n])

      for n in range(len(nums)): # ensure the contents of the array are valid
         if (ord(nums[n]) <= 48 or ord(nums[n]) >= 57):
            return False
      
      for i in range(len(nums)): # turn the array back into a string
         rec_time += str(nums[i])
      
      record_time = int(rec_time) # turn the string into an integer
         
      record_time = int(record_time)

      if record_time >= 0 and record_time <=60: # ensure the length of the string isn't negative or over 60s
         record_audio = record_time
         return True 
      else:
         return False
   
   def getRecordTime(*args) -> int: # getter of record_audio
      global record_audio
      return record_audio
   
   def getSampleRate(*args) -> int:
      return RATE

   def record(*args, **kwargs): # records for specified time
     
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


   def PlayMusic(*args, **kwargs): # plays back the recording
        wav = vlc.MediaPlayer("voice.wav")
        wav.play()