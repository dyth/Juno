#!/usr/bin/env python
"""
Value Network based on Giraffe
"""
from torch.autograd import Variable
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
import torch
torch.manual_seed(1729)
np.random.seed(1729)


class ValueNet(nn.Module):
    """
    Value Network Layers, Architecture and forward pass
    """
    def __init__(self):
        'initialise all the layers and activation functions needed'
        super(ValueNet, self).__init__()

        self.weightsNum = 0
        
        # three layers
        self.fc1 = nn.Linear(9, 64)
        self.fc2 = nn.Linear(64, 9)
        self.fc3 = nn.Linear(9, 1)

        # if cuda, use GPU
        self.gpu = False #torch.cuda.is_available()
        if self.gpu:
            self.cuda()

            
    def list_to_Variable(self, inputLayer):
        'convert a list to Variable for use in PyTorch'
        inputLayer = [0 if iL == None else iL for iL in inputLayer]
        inputLayer = torch.FloatTensor(np.array(inputLayer))
        if self.gpu:
            inputLayer = inputLayer.cuda()
        return Variable(inputLayer)
    
    
    def forward(self, inputLayer):
        'forward pass using Variable inputLayer'
        inputLayer = self.list_to_Variable(inputLayer)
        out = self.fc1(inputLayer)
        out = F.relu(out)
        out = self.fc2(out)
        out = F.relu(out)
        out = self.fc3(out)
        out = F.tanh(out)
        return out.data[0]


    def load_weights(self):
        'load name'
        self.load_state_dict(torch.load("weights.h5"))
    
    
    def save_weights(self, directory):
        'save the weights as the number in directory/'
        self.weightsNum += 1
        name = directory + "/" +  str(self.weightsNum) + ".h5"
        torch.save(self.state_dict(), name)
