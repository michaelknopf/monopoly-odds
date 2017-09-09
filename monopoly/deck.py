class Deck:

    def __init__(self, cards):
        self.position = 0
        self.cards = cards
        self.size = len(cards)

    def draw(self):
        card = self.cards[self.position]
        self.position = (self.position + 1) % self.size
        return card
