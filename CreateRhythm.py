
class CreateRhythm:
    def __init__(self) -> None:
        self.rhythmList = []
        self.timeSig = ""

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
            print(self.timeSig)
            print(self.rhythmList)
        
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


rhythm = CreateRhythm()
rhythm.GetMusic()