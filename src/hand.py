class Hand:
    def __init__(self, cards=None):
        self.cards = cards or []
        self.is_split = False

    def add_card(self, card):
        self.cards.append(card)

    def value(self):
        total = 0
        aces = 0
        for card in self.cards:
            if card in ['J', 'Q', 'K']:
                total += 10
            elif card == 'A':
                aces += 1
                total += 11
            else:
                total += int(card)
        while total > 21 and aces:
            total -= 10
            aces -= 1
        return total

    def is_blackjack(self):
        return len(self.cards) == 2 and self.value() == 21

    def is_bust(self):
        return self.value() > 21

    def is_soft(self):
        return 'A' in self.cards and self.value() <= 21

    def can_split(self):
        return len(self.cards) == 2 and self.cards[0] == self.cards[1]

    def __str__(self):
        return f"{'/'.join(self.cards)} ({self.value()})"