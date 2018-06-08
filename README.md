# Combining Machine Learning Approximator Functions with GOFAI algorithms

Resurgent interest in GOFAI algorithms are partly due to the AlphaGo triumph, which exhibited an architcture using approximator functions to generate values as an input to GOFAI algorithms.

The resolvent combination of techniques reduces the large search tree synonymous with GOFAI algorithms, and nullifies the lack of structure created by deep learning.

This is my attempt at replicating a similar architecture, but on a smaller game, tic-tac-toe. The smaller game would enable better analysis of the effectiveness of this technique. Interesting metrics include learning rate, optimality, how much can a search tree be reduced?

## Prerequisites
* Python 2.7
* Keras

## Value Network

1. Generate training data in the file `value_train.csv` by `python generate_value_training.py`
