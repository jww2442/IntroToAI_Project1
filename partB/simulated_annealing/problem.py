import numpy.random as npr
import numpy as np
import random
import ga_eval

class Problem(object):

    state = [0, 0]

    '''inits x and y val to random float within range of graph '''
    def __init__(self, valueRange, becomesNeg):
        if(becomesNeg == True):
            self.state[0] = npr.random() * valueRange - 0.5*valueRange
            self.state[1] = npr.random() * valueRange - 0.5*valueRange
        else: 
            print('error 493')

    def __init__(self, valRange): 
        self.state[0] = npr.random() * valRange
        self.state[1] = npr.random() * valRange

    #returns next state based on standard distribution
    def successor(self, curState, minRange, maxRange):
        outOfBounds = True
        while(outOfBounds):
            nextState = [random.gauss(0,1)*curState[0], random.gauss(0,1)*curState[1]]
            outOfBounds = False
            if(nextState[0]<minRange or nextState[0]>maxRange or nextState[1]<minRange or nextState[1]>maxRange):
                outOfBounds = True

        return nextState

    def calculateFuncValue(self, state):
        input = np.array(state)
        output = ga_eval.sphere(input)

        return output

    def calculateBumpValue(self, state):
        input = np.array(state)
        output = ga_eval.bump(input)

        return output