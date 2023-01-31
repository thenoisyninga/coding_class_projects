
class TreasureChest:

    # DECLARE question : STRING
    # DECLARE answer : INTEGER
    # DECLARE points : INTEGER

    def __init__(self, questionP, answerP, pointsP):
        self.question = questionP
        self.answer = answerP
        self.points = pointsP

    def getQuestion(self):
        return self.question

    def checkAnswer(self, userAnswer):
        if userAnswer == self.answer:
            return True
        else:
            return False

    def getPoints(self):
        return self.points