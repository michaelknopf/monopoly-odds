class Board:

    def __init__(self, square_names):
        self.square_names = square_names
        self.name_to_position = {square_names[i]: i for i in range(len(square_names))}
        self.size = len(self.square_names)

    def get_next_railroad_position(self, position):
        while not self.is_railroad(position):
            position = (position + 1) % self.size
        return position

    def is_railroad(self, position):
        return self.square_names[position][0] == 'R'

    def get_next_utility_position(self, position):
        while not self.is_utility(position):
            position = (position + 1) % self.size
        return position

    def is_utility(self, position):
        return self.square_names[position][0] == 'U'
