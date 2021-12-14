import numpy as np


def createRandBitString(stringLen):
    bitString = ''
    for i in range(stringLen):
        bit = np.random.randint(0,2)
        bitString = bitString + str(bit)
    
    return bitString


def createOrganism(numChromosome, bitStrLen):

    organism = []

    for i in range(numChromosome):
        organism.append(createRandBitString(bitStrLen))

    return organism


def createInitialPopulation(popSize, numChrom, bitStrLen):
    pop = []

    for i in range(popSize):
        pop.append(createOrganism(numChrom, bitStrLen))

    return pop

