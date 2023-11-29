
class feedback():
    def __init__(self) -> None:
        self.feedbackValues : list = []
        self.fValues : list = [1,2,3]
        self.messages : list = []
        self.score = 0
    
    def setFeedbackValues(self, fVal : list) -> None:
        for i in range(len(fVal)):
            if not(fVal[i] in self.fValues):
                return
        self.feedbackValues = fVal
    
    def giveFeedback(self) -> None:
        for i in range(len(self.feedbackValues)):
            match i:
                case 1:
                    self.messages.append("Beat in time")
                case 2:
                    self.messages.append("Beat slightly off time")
                case 3:
                    self.messages.append("Beat off time")
        x = 0
        for i in range(len(self.feedbackValues)):
            match i:
                case 1:
                    x += 1 / len(self.feedbackValues)
                case 2:
                    x += 1 / (2 * len(self.feedbackValues))
                case 3:
                    x += 1 / (3 * len(self.feedbackValues))
        self.score = x * 100
