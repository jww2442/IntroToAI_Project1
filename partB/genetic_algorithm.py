from unit_tests import chooseFunctionTest
import numpy as np
import random

def geneticAlgorithm(population, numParents, mutationChance, numGenerations, funcName):

    numIterations = 0
    fitness = []

    #creates a new generation after each iteration
    while(numIterations < numGenerations):

        fitness = testOrganisms(population, funcName)

        population2 = []

        #creates a new child in pop2 after each iteration
        for i in range(len(population)):

            parentIndices = parentSelection(fitness, numParents, 10)

            child = reproduce(population, parentIndices, 52)

            #does this work? 
            if(mutationChance > np.random.random()):
                child = mutate(child, 52)
            
            population2.append(child)
            
        population = population2

        numIterations +=1

    return [population[0], fitness[0]]

#return list of tuples, containing inidices of organisms and results of running on given function
def testOrganisms(pop, function):
    results = []
    for i in range(len(pop)):
        results.append((i, chooseFunctionTest(function, pop[i])))
    return results

#returns indices of new parents
def parentSelection(fitnesses, numParents, groupSize):
    
    randGroup = random.sample(fitnesses, groupSize)
    randGroup.sort(key = lambda x: x[1])

    parents = []
    for i in range(numParents):
        parents.append(randGroup[i][0])
    return parents
    
#returns new child
'''currently only works with 2 parents'''
def reproduce(population, parentIndices, bitStrLen):
    parentOrgs = []
    for i in range(len(parentIndices)):
        parentOrgs.append(population[parentIndices[i]])
    
    crossOverPoint = np.random.randint(0,bitStrLen)

    newXBitStr = parentOrgs[0][0][0: crossOverPoint] + parentOrgs[1][0][crossOverPoint:bitStrLen]
    newYBitStr = parentOrgs[0][1][0: crossOverPoint] + parentOrgs[1][1][crossOverPoint:bitStrLen]

    return [newXBitStr, newYBitStr]

def mutate(org, bitStrLen):

    mutLoc = np.random.randint(0,bitStrLen)
    x = list(org[0])
    y = list(org[1])

    if(x[mutLoc] == '0'):
        x[mutLoc] = '1'
    elif(x[mutLoc] == '1'):
        x[mutLoc] = '0'
    else:
        print('ERROR 19')

    if(y[mutLoc] == '0'):
        y[mutLoc] = '1'
    elif(y[mutLoc] == '1'):
        y[mutLoc] = '0'
    else:
        print('ERROR 199')

    newOrg = [''.join(x), ''.join(y)]

    return newOrg