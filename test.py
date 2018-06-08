#!/usr/bin/env python
"""play noughts and crosses against a random agent or human opposition"""
from minimax import *
from noughts_crosses import *


if __name__ == "__main__":
    e = Engine(optimal, 9)
    print e.minimax(initialBoard, players[0])
