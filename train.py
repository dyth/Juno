#!/usr/bin/env python



def load_weights():
    'load name into valueNetwork'
    name = "214.h5"
    valueNetwork.load_state_dict(torch.load(name))


def save_weights(directory):
    'save the weights as the number in treeStrapWeights/'
    global weightsNum
    weightsNum += 1
    name = directory + "/" +  str(weightsNum) + ".h5"
    torch.save(valueNetwork.state_dict(), name)
