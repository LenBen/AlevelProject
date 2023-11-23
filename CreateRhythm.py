
class CreateRhythm:
    def __init__(self) -> None:
        self.rhythmList : list = []
        self.timeSig : str = "" 
        self.bpm : int = 120
        self.beatLength = 0 

    def GetMusic(self) -> None:
        with open("O_Output/music.txt", "r") as notes:
            w = notes.read()
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
    
    def setBPM(self, BPM : int):
        if BPM > 0 and BPM < 280:
            self.bpm = BPM
        
    def _getTimeSig(self, w: str) -> str:
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
    
    def _calculateBeatLength(self):
        beatsPerSecond = self.bpm / 60
        self.beatLength = 1 / beatsPerSecond

    def calculateBarLength(self):
        self._calculateBeatLength()
        noOfBeats = ""
        typeOfBeat = ""
        y = 0
        while self.timeSig[y] != "/":
            noOfBeats += self.timeSig[y]
            y += 1
        typeOfBeat = self.timeSig[(y +1):]
        barLength = int(noOfBeats) * self.beatLength
        print(barLength)

