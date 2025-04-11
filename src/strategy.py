class Strategy:
    def __init__(self, strategy_data):
        self.hard = strategy_data.get("hard", {})
        self.soft = strategy_data.get("soft", {})
        self.pair = strategy_data.get("pair", {})

    def get_action(self, hand, dealer_upcard):
        up = str(dealer_upcard)

        if hand.can_split():
            action = self.pair.get(hand.cards[0], {}).get(up)
            if action:
                return action

        if hand.is_soft() and hand.value() >= 13:
            total = str(hand.value())
            action = self.soft.get(total, {}).get(up)
            if action:
                return action

        total = str(hand.value())
        return self.hard.get(total, {}).get(up, "H")
