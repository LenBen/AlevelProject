import subprocess as sp
class CreateRhythm:
    def __init__(self) -> None:
        self.rhythmList : list = []
        self.timeSig : str = "" 
        self.bpm : float = 120
        self.beatLength : float = 0 
        self.lengthArray = []
        self.recLength = 0

    def getBPM(self): # Getter for the BPM
        return self.bpm

    def callOrchestra(*args) -> None: # Calls the orchestra library
        try:
            a = sp.run(["python", "Orchestra/main.py", "O_Input", "O_Output"])
            a.check_returncode()
        except sp.CalledProcessError as err:
            print(err)

    def GetMusic(self) -> None: # adds the rhythms to the rhythm list
        self.callOrchestra()
        with open("O_Output/music.txt", "r") as notes:
            w = notes.read()
            if w[3] == "\\":
                w = self._getTimeSig(w)
            letter = False
            for i in w:
                if not(ord(i) > 46 and ord(i) < 58):
                    letter = True
                elif letter:
                    letter = False
                else:
                    self.rhythmList.append(i)
            self.rhythmList.reverse()
            temp = ""
            tempArray = []
            for i in self.rhythmList:
                if i != "/":
                    temp += i
                else:
                    tempArray.append(temp)
                    temp = ""
            tempArray.reverse()
            self.rhythmList = tempArray
        # self.createLengthArray()
    
    def setBPM(self, BPM : int): # setter for BPM
        if BPM > 0 and BPM < 280:
            self.bpm = BPM
        
    def _getTimeSig(self, w: str) -> str: # Removes the rime signature from the orchestra output and stores it
        i = 0
        timeSig = ''
        write = False
        loop = True
        while loop:
            if w[i] == '>':
                loop = False
                write = False
            if write:
                timeSig += w[i]
            if w[i] == '<':
                write = True
            i+=1
        for j in range(len(timeSig)):
            if ord(timeSig[j]) != 34:
                self.timeSig += timeSig[j]
        w = w[i:]
        return w
    
    def _calculateBeatLength(self): # Caluculates the lenght of a beat in seconds
        beatsPerSecond = float(self.bpm / 60)
        self.beatLength = float(1 / beatsPerSecond)

    def calculateBarLength(self):
        self._calculateBeatLength()
        noOfBeats = ""
        typeOfBeat = ""
        y = 0
        if self.timeSig == "":
            return
        while self.timeSig[y] != "/":
            noOfBeats += self.timeSig[y]
            y += 1
        typeOfBeat = self.timeSig[(y +1):]
        barLength = int(noOfBeats) * self.beatLength
    
        
    def calculateTimeOfNotes(self, *args):
        recLength = []
        for i in range(len(self.rhythmList)):
            recLength.append((self.beatLength / float(self.rhythmList[i])) * 2)
        return recLength
    
    def calculateRecLength(self) -> float:
        recLength = self.calculateTimeOfNotes()
        for i in range(len(recLength)):
            self.recLength += float(recLength[i])
        self.recLength += 0.45 # factor in for the delay of starting
        print(self.recLength)


