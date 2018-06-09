#!/usr/bin/env python
"""play noughts and crosses against a random agent or human opposition"""
from minimax import *
from value_network import *
from noughts_crosses import *


if __name__ == "__main__":
    e = Engine(optimal, 9)
    print e.minimax(initialBoard, players[0])

    
    v = ValueNet()
    e = Engine(v, 2)
    pretty_print(e.minimax(initialBoard, players[0]))
