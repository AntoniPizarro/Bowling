class Bowling():

    # Símbolos que representan tiradas especiales.
    GUTTERBALL = '-'
    SPARE = '/'
    STRIKE = 'X'

    LAST_FRAME = 5
    TOTAL_PINS = 10

    def __init__(self, scorecard):
        # Convertimos el string score_card en una lista.
        self.scorecard = scorecard
        self.score = 0
        self.current_frame = 1
        self.current_roll = 0
        self.rolls_in_frame = 0
        self.special = 0
        self.strike_count = 0

    def game_score(self):
        for roll in self.scorecard:
            if self.current_frame <= self.LAST_FRAME:
                if self.special > 0:
                    self.special -= 1
                    if roll == Bowling.GUTTERBALL:
                        self.score += 0
                    elif roll == Bowling.STRIKE or roll == Bowling.SPARE:
                        self.score += 10 * self.strike_count
                        self.strike_count -= 1
                    elif roll.isdigit():
                        self.score += int(roll)
                if roll.isdigit():
                    Bowling.rollNormal(self, roll)
                elif roll == Bowling.GUTTERBALL:
                    Bowling.rollGutterball(self)
                elif roll == Bowling.SPARE:
                    Bowling.rollSpare(self)
                elif roll == Bowling.STRIKE:
                    Bowling.rollStrike(self)

        return self.score

    def updateRolls(self):
        self.rolls_in_frame += 1
        if self.rolls_in_frame == 2:
            self.current_frame += 1
            self.rolls_in_frame = 0

    def rollNormal(self, score):
        Bowling.updateRolls(self)
        self.current_roll += 1
        self.score += int(score)

    def rollGutterball(self):
        Bowling.updateRolls(self)
        self.score += 0

    def rollSpare(self):
        self.rolls_in_frame += 1
        Bowling.updateRolls(self)
        self.score += 10
        self.special += 1

    def rollStrike(self):
        self.strike_count += 1
        self.rolls_in_frame += 1
        Bowling.updateRolls(self)
        self.score += 10
        self.special = 2

if __name__ == "__main__":
    assert Bowling("63XX11").game_score() == 44