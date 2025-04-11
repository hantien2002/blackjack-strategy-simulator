from deck import Shoe
from strategy import Strategy
from betting import BettingSystem
from game import BlackjackGame
from metrics import Metrics

class Simulation:
    def __init__(self, strategy_data, betting_mode, num_cycles):
        self.strategy = Strategy(strategy_data)
        self.betting_mode = betting_mode
        self.num_cycles = num_cycles

    def run(self):
        all_profits = []
        metrics = Metrics()

        for _ in range(self.num_cycles):
            shoe = Shoe()
            betting = BettingSystem(self.betting_mode)
            game = BlackjackGame(shoe, self.strategy, betting)

            while not shoe.cut_card_reached():
                profit = game.play_hand(metrics)
                all_profits.append(metrics.total_profit)

        return metrics.summary(), all_profits
