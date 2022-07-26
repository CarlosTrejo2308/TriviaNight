class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __str__(self):
        return f"{self.name} {self.score}"

    def __repr__(self):
        return f"Player({self.name}, {self.score})"

    def resetScore(self):
        self.score = 0

    def addScore(self, score):
        self.score += score

    def getScore(self):
        return self.score

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name