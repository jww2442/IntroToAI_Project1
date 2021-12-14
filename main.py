import Item
import NearestNeighbor
import file_io
import os

def main():

    #STORE ALL kNN METHOD BELOW
    N = 5
    k = 5
    fileSize = 1000

    nGroups = file_io.init_groups(fileSize, N)

    storeAllAccuracies = {}

    nn = NearestNeighbor.NearestNeighbor()

    for i in range(N):

        testGroup = nGroups[i]
        testItems = []
        for j in range(len(testGroup)):
            item = Item.Item()
            item.makeLabelItem(testGroup[j])
            testItems.append(item)
        
        
        exampleItems = nn.storeAll(nGroups, i, N, True)

        prediction = nn.predict(testItems, exampleItems, k)

        storeAllAccuracies.update({i+1: nn.calcAccuracy(prediction, testItems)})
    
    printAccuracies(storeAllAccuracies, 'Store All on labeled-examples data')



    #STORE ERRORS kNN METHOD BELOW
    errAccuracies = {}

    for i in range(N):

        exampleErrors = nn.storeErrors(nGroups, i, k, N, True)

        testGroup = nGroups[i]
        testItems = []
        for j in range(len(testGroup)):
            item = Item.Item()
            item.makeLabelItem(testGroup[j])
            testItems.append(item)

        
        prediction2 = nn.predict(testItems, exampleErrors, k)

        acc = nn.calcAccuracy(prediction2, testItems)

        errAccuracies.update({i: acc})
        
    printAccuracies(errAccuracies, 'Store Errors on labeled-examples data')

    

    
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'kNN_data\\shuttleData\\shuttle.tst')

    print('NOTE: This one might take a few minutes. ')
    ### ###
    size = 5000
    N = 5
    k = 5
    nGroupsShuttle = file_io.init_groups(size, N, filename)
    
    shuttleAccuracy = {}

    for i in range(N):

        testGroup = nGroupsShuttle[i]
        testItems = []
        for j in range(len(testGroup)):
            item = Item.Item()
            item.makeShuttleItem(testGroup[j])
            testItems.append(item)
        
        exampleItems = nn.storeAll(nGroupsShuttle, i, N, False)

        prediction3 = nn.predictShuttle(testItems, exampleItems, k)

        shuttleAcc = nn.calcShuttleAccuracy(prediction3, testItems)

        shuttleAccuracy.update({i: shuttleAcc})

    printAccuracies(shuttleAccuracy, 'Store All on shuttle data')





def printAccuracies(accDict, storeType):

    sumAcc = 0
    for i, value in enumerate(accDict):
        print('Accuracy of', storeType, 'for Test Group', i + 1, ': ', accDict.get(value))
        sumAcc +=accDict.get(value)
    print('Average accuracy of', storeType, ':', sumAcc/5, '\n')





main()