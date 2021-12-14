import numpy as np
import numpy.random as npr
import math
import problem
import schedule

def simulatedAnnealing(problem, sched, funcMinRange, funcMaxRange):

    currentState = problem.state

    i = 0
    while(True):
        T = sched.schedule[i]
        i+=1

        if(T <= 0):
            return currentState
        
        nextState = problem.successor(currentState, funcMinRange, funcMaxRange)

        deltE = problem.calculateBumpValue(currentState) - problem.calculateBumpValue(nextState)

        if(deltE > 0):
            currentState = nextState
        else:
            if(math.e**(deltE / T) > npr.random()):
                currentState = nextState
            

def main():

    #bump graph
    prob1 = problem.Problem(5)

    #sphere graph
    prob2 = problem.Problem(8)

    #linear schedule
    initTemp = 10000
    finalTemp = 0
    delta = 1
    schedule1 = schedule.Schedule(initTemp, finalTemp, delta)

    #exponential schedule
    initTemp = 5000
    schedule2 = schedule.Schedule(0, 0)
    schedule2.makeExponentialSched(initTemp)



    finalState = simulatedAnnealing(prob1, schedule1, 0, 5)
    print("Minimum state found for Bump Function using linear-schedule simulated annealing: {}\n".format(finalState))

    

    finalState = simulatedAnnealing(prob2, schedule1, -4, 4)
    print("Minimum state found for Sphere Function using linear-schedule simulated annealing: {}\n".format(finalState))



    finalState = simulatedAnnealing(prob1, schedule2, 0, 5)
    print("Minimum state found for Bump Function using exponential-schedule simulated annealing: {}\n".format(finalState))


    finalState = simulatedAnnealing(prob2, schedule2, -4, 4)
    print("Minimum state found for Sphere Function using exponential-schedule simulated annealing: {}\n".format(finalState))

main()