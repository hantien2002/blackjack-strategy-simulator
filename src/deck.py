import random

class Shoe:
    def __init__(self, num_decks=6, cut_card_ratio=0.75):
        self.num_decks = num_decks
        self.cut_card_position = int(52 * num_decks * cut_card_ratio)
        self.cards = []
        self.position = 0
        self._build_shoe()

    def _build_shoe(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = ranks * 4 * self.num_decks
        random.shuffle(self.cards)
        self.position = 0

    def draw_card(self):
        if self.position >= len(self.cards):
            self._build_shoe()
        card = self.cards[self.position]
        self.position += 1
        return card

    def cut_card_reached(self):
        return self.position >= self.cut_card_position
