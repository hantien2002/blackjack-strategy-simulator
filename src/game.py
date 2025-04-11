from hand import Hand

class BlackjackGame:
    def __init__(self, shoe, strategy, betting):
        self.shoe = shoe
        self.strategy = strategy
        self.betting = betting

    def play_hand(self, metrics):
        bet = self.betting.next_bet()
        player = Hand([self.shoe.draw_card(), self.shoe.draw_card()])
        dealer = Hand([self.shoe.draw_card(), self.shoe.draw_card()])
        dealer_up = dealer.cards[0]
        hands = [(player, bet)]
        final_profit = 0

        while hands:
            hand, stake = hands.pop()
            result = None
            profit = 0

            if hand.is_blackjack():
                if dealer.is_blackjack():
                    result = "push"
                    profit = 0
                else:
                    result = "blackjack"
                    profit = 1.5 * stake
            else:
                while True:
                    move = self.strategy.get_action(hand, dealer_up)
                    metrics.moves[move] += 1
                    if move == "H":
                        hand.add_card(self.shoe.draw_card())
                        if hand.is_bust():
                            result = "loss"
                            profit = -stake
                            break
                    elif move == "S":
                        break
                    elif move == "D":
                        stake *= 2
                        hand.add_card(self.shoe.draw_card())
                        break
                    elif move == "P" and hand.can_split():
                        h1 = Hand([hand.cards[0], self.shoe.draw_card()])
                        h1.is_split = True
                        h2 = Hand([hand.cards[1], self.shoe.draw_card()])
                        h2.is_split = True
                        hands.append((h2, stake))
                        hands.append((h1, stake))
                        metrics.moves['split'] += 1
                        break
                    elif move == "N":
                        break

                if result is None:
                    while dealer.value() < 17 or (dealer.value() == 17 and dealer.is_soft()):
                        dealer.add_card(self.shoe.draw_card())
                    if hand.is_bust():
                        result = "loss"
                        profit = -stake
                    elif dealer.is_bust() or hand.value() > dealer.value():
                        result = "win"
                        profit = stake
                    elif hand.value() < dealer.value():
                        result = "loss"
                        profit = -stake
                    else:
                        result = "push"
                        profit = 0

            metrics.results[result] += 1
            final_profit += profit
            metrics.record(profit, stake)
            self.betting.record_outcome(result if result in ["win", "loss"] else "push")

        return final_profit
