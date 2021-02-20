class Frame:
    def __init__(self, frame_score, rolls, strike, last_frame):
        self.frame_score = frame_score
        self.rolls = rolls
        self.strike = strike
        self.last_frame = last_frame

    def concluded(self):
        if self.strike == True or self.rolls == 2 and self.last_frame == False or self.rolls == 3 and self.last_frame == True:
            return True
        else:
            return False

    def addScore(self, score):
        self.frame_score += score
        return self.frame_score