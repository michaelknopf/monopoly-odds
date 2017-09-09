import random
from . import Board, Dice, Deck, Game, data


def count_square_frequencies(game, moves):
    position_frequencies = [0 for i in range(len(game.board.square_names))]
    for i in range(moves):
        game.move()
        position_frequencies[game.position] += 1
    return position_frequencies


def get_position_rankings(position_frequencies):
    return sorted(enumerate(position_frequencies), key=lambda x:-x[1])


def get_position_proportions(position_frequencies):
    total = sum(position_frequencies)
    proportions = [freq / total for freq in position_frequencies]
    return sorted(enumerate(proportions), key=lambda x: -x[1])


def rank_squares(dice_sides=(6, 6), moves=10**6):

    game = Game(
        board=Board(
            square_names=data['board']
        ),
        dice=Dice(
            dice_sides=dice_sides
        ),
        decks={
            'CC': Deck(
                cards=data['chest'] + [None for i in range(14)]
            ),
            'CH': Deck(
                cards=data['chance'] + [None for i in range(6)]
            )
        }
    )
    for _, deck in game.decks.items():
        random.shuffle(deck.cards)

    frequencies = count_square_frequencies(game, moves)
    return get_position_rankings(frequencies)
