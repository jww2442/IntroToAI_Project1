import numpy as np
import random
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'labeled-examples.txt')

'''inputs num of lines/items in text file (fileSize), num of partitions for those items (N), and the num of the group that is to be tested (testGroup)'''
'''outputs a list containing item objects'''
def init_groups(fileSize, N, path = filename):
    with open(path) as f:
        file = f.read().splitlines(True)

    random.shuffle(file)
    
    groupSize = fileSize//N
    nGroups = []
    for i in range(N):
        nGroups.append(file[groupSize*i : groupSize*(i+1)])
        #this is = to [file[0:200], file[200:400], file[400:600], file[600:800], file[800:1000]]

    return nGroups