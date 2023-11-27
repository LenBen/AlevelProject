
class feedback():
    def __init__(self) -> None:
        self.feedbackValues = []
        self.fValues = [1,2,3]
    
    def setFeedbackValues(self, fVal : list):
        for i in range(len(fVal)):
            if not(fVal[i] in self.fValues):
                return
        self.feedbackValues = fVal