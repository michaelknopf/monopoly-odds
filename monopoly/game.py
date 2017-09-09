class Game:

    def __init__(self, board, dice, decks, position=0):
        self.position = position
        self.board = board
        self.dice = dice
        self.decks = decks
        self.consecutive_doubles = 0

    def advance(self, squares):
        self.position = (self.position + squares) % self.board.size

    @staticmethod
    def is_doubles(roll):
        for i in range(1, len(roll)):
            if roll[i] != roll[i-1]:
                return False
        return True

    def move(self):
        roll = self.dice.roll()

        if self.is_doubles(roll):
            self.consecutive_doubles += 1
            if self.consecutive_doubles == 3:
                self.consecutive_doubles = 0
                self.position = self.board.name_to_position['JAIL']
                return
        else:
            self.consecutive_doubles = 0

        self.advance(sum(roll))

        square_name = self.board.square_names[self.position]
        if square_name[:-1] in self.decks:
            card = self.decks[square_name[:-1]].draw()
            self.resolve_card(card)
        elif square_name == 'G2J':
            self.position = self.board.name_to_position['JAIL']

    def resolve_card(self, card):
        if card is None:
            return
        elif card == 'next_R':
            self.go_to_next_railroad()
        elif card == 'next_U':
            self.go_to_next_utility()
        elif card == 'back_3':
            self.advance(-3)
        else:
            self.go_to_square_name(card)

    def go_to_next_railroad(self):
        self.position = self.board.get_next_railroad_position(self.position)

    def go_to_next_utility(self):
        self.position = self.board.get_next_utility_position(self.position)

    def go_to_square_name(self, square_name):
        self.position = self.board.name_to_position[square_name]
