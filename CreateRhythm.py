import subprocess as sp
import step2
class CreateRhythm:
    def __init__(self) -> None:
        self.rhythmArray : list = []
        self.lengthArray : list = []
        self.timeSig : str = "" 
        self.bpm : int = 120
        self.beatType : int = 4
        self.beatLength : float = 0 
        self.recLength : float = 0

    def getBPM(self) -> int: # Getter for the BPM
        return self.bpm

    def setBPM(self, BPM : int) -> None: # setter for BPM
        if BPM > 0 and BPM < 280:
            self.bpm = int(BPM)
        else:
            raise TypeError
    
    def getLengthArray(self) -> list:
        return self.lengthArray
        
    def callOrchestra(*args) -> None: # Calls the orchestra library
        try:
            a = sp.run(["python", "Orchestra/main.py", "O_Input", "O_Output"])
            a.check_returncode()
        except sp.CalledProcessError as err:
            print(err)

    def GetMusic(self) -> None: # adds the rhythms to the rhythm list
        self.callOrchestra()
        with open("O_Output/music.txt", "r") as notes:
            o_Output : str = notes.read()

            if o_Output[2] == "\\": # Checks for time signature
                o_Output = self._getTimeSig(o_Output)

            letter = False
            for i in o_Output:
                if not(ord(i) > 46 and ord(i) < 58): # Filtering out blank spaces and letters
                    letter = True
                elif letter:
                    letter = False
                else:
                    self.rhythmArray.append(i)
                
            self.rhythmArray.reverse()
            temp = ""
            tempArray = []
            for i in self.rhythmArray: # Getting just numbers
                if i != "/":
                    temp += i
                else:
                    tempArray.append(temp)
                    temp = ""
            tempArray.reverse()

            for i in range(len(tempArray)): # Reverses each value so they are not backwards
                tempArray[i] = tempArray[i][::-1]

            self.rhythmArray = tempArray
    
    def _getTimeSig(self, o_Output: str) -> str: # Removes the rime signature from the orchestra output and stores it
        i : int = 0
        timeSig : str = ''
        write : bool = False
        loop : bool = True

        while loop: # Gets rid of the < and > symbols
            if o_Output[i] == '>':
                loop = False
                write = False
            if write:
                timeSig += o_Output[i]
            if o_Output[i] == '<':
                write = True
            i+=1

        for j in range(len(timeSig)): # Gets rid of quotation marks so that just the time sig is left
            if ord(timeSig[j]) != 34:
                self.timeSig += timeSig[j]

        o_Output = o_Output[i:] # Splits the output
        return o_Output

    def calculateBeatLength(self) -> None: # Caluculates the lenght of a beat in seconds
        self._calculateBeatValue()

        beatsPerSecond = float(self.bpm / 60)
        beatLength = float(1 / beatsPerSecond)

        self.beatLength = beatLength * (4 / self.beatType)

    def _calculateBeatValue(self) -> None:  # Calculates the type of beat
        if self.timeSig == "":
            return None
        
        slash : bool = False
        beat : str = ""
        i : int = -1

        while not slash: # This loops over the time sig to get the last number in the time sig
            if self.timeSig[i] != "/":
                beat += self.timeSig[i]
                i -= 1
            else:
                slash = True
        
        self.beatType = int(beat)

    def _createLengthArray(self) -> None: # This creates the length array with time length instead of beat length
        for i in range(len(self.rhythmArray)):
            self.lengthArray.append((self.beatLength / float(self.rhythmArray[i])) * 4)    

    def calculateRecLength(self) -> None: # Calculates the recording length
        self._createLengthArray()
        for i in range(len(self.lengthArray)):
            self.recLength += float(self.lengthArray[i])
        self.recLength += 1.45 # factor in for the delay of starting
        step2.audio.setRecordTime(self.recLength)
