from ga_util import bitstr2float
from organism import createInitialPopulation
import genetic_algorithm

def printResults(funcTest, finalPop, numGenerations, mutationChance):
    print('Function:', funcTest, '\n\tNumber of iterations of Genetic Algorithm:', numGenerations, '\nChance of mutation: ', mutationChance, '\n\tFittest bit-string pair:', finalPop[0], '\n\tResulting input: [', bitstr2float(finalPop[0][0]), ', ', bitstr2float(finalPop[0][1]), ']\n\tResulting output on', funcTest, 'function:', finalPop[1][1], '\n\n')

def main():

    functionNames = ['sphere', 'shekel', 'langermann', 'bump']

    populationSize = 500
    chromosomeCount = 2
    bitStrLength = 52
    population1 = createInitialPopulation(populationSize, chromosomeCount, bitStrLength)


    mutationChance = 0.001
    numGenerations = 500

    for funcTest in functionNames:
        
        finalPop = genetic_algorithm.geneticAlgorithm(population1, 2, mutationChance, numGenerations, funcTest)

        printResults(funcTest, finalPop, numGenerations, mutationChance)


def modifiedRates(newMutateRate, newNumGenerations):
    populationSize = 500
    chromosomeCount = 2
    bitStrLength = 52
    population = createInitialPopulation(populationSize, chromosomeCount, bitStrLength)


    func = 'sphere'
    finalPop = genetic_algorithm.geneticAlgorithm(population, 2, newMutateRate, newNumGenerations, func)

    printResults(func, finalPop, newNumGenerations, newMutateRate)



main()

print('\n\nMODIFIED RATES: ')
mutateRates = [0, 0.1, 1]
for i in mutateRates:

    modifiedRates(i, 500)