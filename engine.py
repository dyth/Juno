#!/usr/bin/env python
"""engine utilises a function policy to choose the best move using minimax"""
from noughts_crosses import *


class Engine:

    def __init__(self, policy, searchDepth):
        'initialise with a policy function and the maximum search depth of '
