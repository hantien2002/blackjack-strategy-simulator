from collections import defaultdict

class Metrics:
    def __init__(self):
        self.results = defaultdict(int)
        self.moves = defaultdict(int)
        self.hands_played = 0
        self.total_profit = 0
        self.total_wagered = 0

    def record(self, profit, bet):
        self.total_profit += profit
        self.total_wagered += bet
        self.hands_played += 1

    def summary(self):
        win = self.results['win']
        loss = self.results['loss']
        push = self.results['push']
        bj = self.results['blackjack']
        total = win + loss + push + bj
        return {
            'win %': round(100 * win / total, 2) if total else 0,
            'loss %': round(100 * loss / total, 2) if total else 0,
            'push %': round(100 * push / total, 2) if total else 0,
            'blackjack %': round(100 * bj / total, 2) if total else 0,
            'moves': dict(self.moves),
            'total hands': total,
            'total profit ($)': round(self.total_profit, 2),
            'total units wagered': self.total_wagered / 100,
            'ROI': round(self.total_profit / self.total_wagered, 4) if self.total_wagered else 0
        }
