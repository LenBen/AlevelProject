
class CreateRhythm:
    def __init__(self) -> None:
        self.rhythmArray = []

    def GetMusic(self):
        with open("O_Output/music.txt", "r") as notes:
            w = notes.read()
            letter = False
            for i in w:
                if not(ord(i) > 46 and ord(i) < 58):
                    letter = True
                elif letter:
                    letter = False
                else:
                    self.rhythmArray.append(i)
            self.rhythmArray.reverse()
            temp = ""
            tempArray = []
            for i in self.rhythmArray:
                if i != "/":
                    temp += i
                else:
                    tempArray.append(temp)
                    temp = ""
            tempArray.reverse()
            self.rhythmArray = tempArray
            print(self.rhythmArray)

rhythm = CreateRhythm()
rhythm.GetMusic()