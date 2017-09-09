class Game:
    def __init__(self, board, dice, decks):
        self.position = 0
        self.board = board
        self.dice = dice
        self.decks = decks

    def move(self):
        self.position += self.dice.roll()
        square_name = self.board.square_names[self.position]
        if square_name in self.decks:
            card = self.decks[square_name].draw()
            self.resolve_card(card)

    def resolve_card(self, card):
        if card == 'next_R':
            self.go_to_next_railroad()
        elif card == 'next_U':
            self.go_to_next_utility()
        elif card == 'back_3':
            self.position -= 3
        else:
            self.go_to_square_name(card)

    def go_to_next_railroad(self):
        self.position = self.board.get_next_railroad_position(self, self.position)

    def go_to_next_utility(self):
        self.position = self.board.get_next_utility_position(self, self.position)

    def go_to_square_name(self, square_name):
        self.position = self.board.name_to_position[square_name]
