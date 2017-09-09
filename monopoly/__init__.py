import yaml
import os

with open(os.path.join(os.path.dirname(__file__), 'data.yaml'), 'r') as f:
    data = yaml.load(f)

from .game import Game
from .board import Board
from .deck import Deck
from .dice import Dice
from .odds import rank_squares