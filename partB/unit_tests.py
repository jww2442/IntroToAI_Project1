from organism import createOrganism
import ga_eval
import ga_util
import numpy as np

def makeInputsFromOrganism(org, minIn, maxIn):

    flts = []
    diff = maxIn - minIn
    for i in range(len(org)):
        flt = ga_util.bitstr2float(org[i])
        flt = flt * diff - diff/2
        flts.append(flt)

    arr = np.array(flts)
    return arr


def chooseFunctionTest(funcName, org):
    output = 0
    if(funcName == 'sphere'):
        input = makeInputsFromOrganism(org, -5, 5)
        output = ga_eval.sphere(input)
    if(funcName == 'griew'):
        input = makeInputsFromOrganism(org, 0, 200)
        output = ga_eval.griew(input)
    if(funcName == 'shekel'):
        input = makeInputsFromOrganism(org, 0, 10)
        output = ga_eval.shekel(input)
    if(funcName == 'micha'):
        input = makeInputsFromOrganism(org, -100, 100)
        output = ga_eval.micha(input)
    if(funcName == 'langermann'):
        input = makeInputsFromOrganism(org, 0, 10)
        output = ga_eval.langermann(input)
    if(funcName == 'odd_square'):
        input = makeInputsFromOrganism(org, -5*np.pi, 5*np.pi)
        output = ga_eval.odd_square(input)
    if(funcName == 'bump'):
        input = makeInputsFromOrganism(org, 0, 100)
        output = ga_eval.bump(input)

    return output
