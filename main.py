import random

from game import Game
from hero import Hero

human = Hero("Победитель", 100, random.randint(80,85))
computer = Hero("Проигравший", 100, random.randint(0,10))

game = Game()
game.start(human, computer)