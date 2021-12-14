import numpy as np

class Schedule(object):
    initialTemp = 0
    finalTemp = 0
    delta = 0

    schedule = []

    def __init__(self, initialT, finalT, delta = 1):
        self.initialTemp = initialT
        self.finalTemp = finalT
        self.delta = delta

        for i in range((initialT - finalT)//delta):
            self.schedule.append(initialT - delta*i)
        self.schedule.append(0)
        
    def printAll(self):
        print('''initial Temp: {}\nfinal: {}\ndelta: {}\ntotal schedule: {}'''.format(self.initialTemp, self.finalTemp, self.delta, self.schedule))

    def makeExponentialSched(self, initialTemp):
        self.schedule = []
        self.schedule.append(initialTemp)
        while(initialTemp>1):
            initialTemp = initialTemp * 0.99
            self.schedule.append(initialTemp)

        self.schedule.append(0)
        return self.schedule