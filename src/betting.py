class BettingSystem:
    def __init__(self, mode):
        self.mode = mode
        self.base_bet = 100
        self.win_streak = 0
        self.current_bet = self.base_bet

    def next_bet(self):
        if self.mode == "flat":
            return self.base_bet
        elif self.mode == "streak":
            return self.current_bet

    def record_outcome(self, result):
        if self.mode != "streak":
            return
        if result == "win":
            self.win_streak += 1
            if self.win_streak == 2:
                self.current_bet *= 2
            elif self.win_streak > 2:
                self.current_bet = min(self.current_bet * 2, 800)
        else:
            self.win_streak = 0
            self.current_bet = self.base_bet
