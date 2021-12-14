import Item
import math

#NN CLASS
class NearestNeighbor(object):
    def __init__(self):
        pass

    '''inputs all 5 groups (list of lists), the loc of the test group (int), and the number of total groups (int). 
    outputs all 4 example groups combined in a list of Item objects. '''
    def storeAll(self, nGroups, testGroupNum, N, defaultData):

        #combines all example groups together
        exampleGroups = []
        for i in range(N):
            if(i==testGroupNum):
                continue
            exampleGroups.extend(nGroups[i])

        #creates new list of item objects to replace example groups
        exampleItems = []
        if(defaultData):
            for i in range(len(exampleGroups)):
                item = Item.Item()
                item.makeLabelItem(exampleGroups[i])
                exampleItems.append(item)
                
        elif(not defaultData):
            for i in range(len(exampleGroups)):
                item = Item.Item()

                item.makeShuttleItem(exampleGroups[i])

                
                exampleItems.append(item)


        return exampleItems


    def storeErrors(self, nGroups, testGroupNum, k, N, defaultData):

        exampleItems = self.storeAll(nGroups, testGroupNum, N, defaultData)
        errors = []

        count0 = 0
        count1 = 0
        lastEx = 0
        for i in range(len(exampleItems)):
            if(exampleItems[i].label == 0 and count0 < 5):
                count0+=1
                errors.append(exampleItems[i])
            elif(exampleItems[i].label == 1 and count1 < 5):
                count1 += 1
                errors.append(exampleItems[i])
            elif(count0 >= 5 and count1 < 5 and exampleItems[i].label == 0):
                continue
            elif(count1 >= 5 and count0 < 5 and exampleItems[i].label == 1):
                continue
            elif(count1 >= 5 and count0 >= 5):
                lastEx = i
                break
            else:
                print('ERROR51')
                break

        #considers further potential examples one at a time
        for ex in exampleItems[lastEx:len(exampleItems) - lastEx]:

            close = []
            for i in range(k):
                close.append((0,1))

            farthestDiff = 1
            farthestIndex = 0

            for er in errors:

                XRdiff = math.sqrt((ex.xVal-er.xVal)**2 + (ex.yVal - er.yVal)**2)
                
                if(XRdiff < farthestDiff):
                    close[farthestIndex] = (er.label, XRdiff)

                    farthestDiff = 0
                    farthestIndex = 0
                    for i in range(k):
                        if(close[i][1] > farthestDiff):
                            farthestDiff = close[i][1]
                            farthestIndex = i
            
            zeroCount = 0
            oneCount = 0
            for i in range(k):
                if(close[i][0] == 0):
                    zeroCount +=1
                elif(close[i][0] == 1):
                    oneCount += 1
                else: 
                    print("ERROR11")
            
            guess = -1
            if(zeroCount > oneCount):
                guess = 0
            elif(oneCount>zeroCount):
                guess = 1
            else:
                print("error90")

            if(guess == ex.label):
                continue
            elif(guess != ex.label):
                errors.append(ex)
        

        return errors
        

    def predict(self, testItems, exampleItems, k):

        #print(testItems)
        predict = []

        for t in range(len(testItems)):

            close = []
            for i in range(k):
                close.append((0,1))

            farthestDiff = 1
            farthestIndex = 0

            for e in range(len(exampleItems)):
                TEdiff = math.sqrt((testItems[t].xVal-exampleItems[e].xVal)**2 + (testItems[t].yVal - exampleItems[e].yVal)**2)
                

                if(TEdiff < farthestDiff):
                    close[farthestIndex] = (exampleItems[e].label, TEdiff)

                    farthestIndex = 0
                    farthestDiff = 0
                    for i in range(k):
                        if(close[i][1] > farthestDiff):
                            farthestDiff = close[i][1]
                            farthestIndex = i
            zeroCount = 0
            oneCount = 0

            for i in range(k):
                if(close[i][0] == 0):
                    zeroCount +=1
                elif(close[i][0] == 1):
                    oneCount += 1
                else: 
                    print("ERROR1")
                

            #print("zero: {} \none: {}".format(zeroCount, oneCount))
            
            if(zeroCount > oneCount):
                predict.append(0)
            elif(oneCount>zeroCount):
                predict.append(1)
            else:
                print("error2")


        return predict

    def calcAccuracy(self, prediction, testItems):
        correct = 0
        incor = 0
        if(len(prediction) != len(testItems)):
            print("ERROR33")
        for i in range(len(prediction)):
            if(prediction[i] == testItems[i].label):
                correct+=1
            elif(prediction[i] != testItems[i].label):
                incor+=1
        return correct/(correct+incor)

    def most_frequent(self, List): 
            counter = 0
            num = List[0] 
            
            for i in List: 
                curr_frequency = List.count(i) 

                if(curr_frequency > counter): 

                    counter = curr_frequency 
                    num = i
        
            return num 


    def predictShuttle(self, testItems, exampleItems, k):
        
        predict = []

        for t in testItems:

            close = []
            for i in range(k):
                close.append((0,1000))

            farthestDiff = 1000
            farthestIndex = 0

            for e in exampleItems:
                squaredSum = 0
                for i in range(len(e.shuttleInputData)):
                    squaredSum += (t.shuttleInputData[i] - e.shuttleInputData[i])**2
                TEdiff = math.sqrt(squaredSum)
                

                if(TEdiff < farthestDiff):
                    close[farthestIndex] = (e.shuttleClass, TEdiff)

                    farthestIndex = 0
                    farthestDiff = 0
                    for i in range(k):
                        if(close[i][1] > farthestDiff):
                            farthestDiff = close[i][1]
                            farthestIndex = i
            
            kNear = []
            for i in range(len(close)):
                kNear.append(close[i][0])
                
            pluralityLabel = self.most_frequent(kNear)
                            
            predict.append(pluralityLabel)


        return predict
    
    def calcShuttleAccuracy(self, prediction, testItems):
        correct = 0
        incor = 0
        if(len(prediction) != len(testItems)):
            print("ERROR33")
        for i in range(len(prediction)):
            if(prediction[i] == testItems[i].shuttleClass):
                correct+=1
            elif(prediction[i] != testItems[i].label):
                incor+=1
        return correct/(correct+incor)




############################################################################################
