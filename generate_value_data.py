#!/usr/bin/env python
"""create train_value.csv on game tree"""
from node import *
import csv, random


def square_to_vector_encoding(sq):
    'convert the square to encodings accordingly, getting rid of None values'
    if sq == None:
        return 0
    if sq == 0:
        return -1
    else:
        return 1


def generate_training_pair(currentNode):
    'breadth-first search through the node to generate pairs'
    global datapoints
    if currentNode != None:
        board = [square_to_vector_encoding(sq) for sq in currentNode.board]
        # write row in global trainingPairs
        datapoints.add(tuple([str(i) for i in board + currentNode.pWins]))
        # recursion for other nodes
        if currentNode.moves != []:
            for n in currentNode.moves:
                generate_training_pair(n)


# generate tree of all distinct boards and values, convert to list and shuffle
datapoints = set()
root = value_node(0, initialBoard)
generate_training_pair(root)

print "In total, there are", len(datapoints), "datapoints"
datapoints = list(datapoints)
random.shuffle(datapoints)

print "Create training set with", len(datapoints) - 200, "datapoints"
with open("value_train.csv", 'wb') as openFile:
    csv.writer(openFile).writerows(datapoints[:200])

print "Create validation set with", 200, "datapoints"
with open("value_validate.csv", 'wb') as openFile:
    csv.writer(openFile).writerows(datapoints[200:])
