#ITEM CLASS
class Item(object):
    label = 0
    xVal = 0.0
    yVal = 0.0
    itemNum = ''

    #these two vars only used if item contains shuttle data from the external database
    shuttleInputData = []
    shuttleClass = 0

    def __init__(self):
        pass

    def makeLabelItem(self, lineText):
        
        forward = 0
        back = 0
        num = 0
        

        for char in lineText: 
            if(char.isspace()):
                if(num==0):
                    self.label = int(lineText[back:forward])
                if(num==1):
                    self.xVal = float(lineText[back:forward])
                if(num==2):
                    self.yVal = float(lineText[back:forward])
                if(num==3):
                    self.itemNum = lineText[back:forward]
                    break

                back = forward + 1
                num+=1
                
            forward+=1 


    def makeShuttleItem(self, lineText):
        self.shuttleInputData = []
        forward = 0
        back = 0
        num = 0
        
        for char in lineText: 
            if(char.isspace()):
                if(num==0):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==1):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==2):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==3):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==4):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==5):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==6):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==7):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==8):
                    self.shuttleInputData.append(int(lineText[back:forward]))
                if(num==9):
                    self.shuttleClass = int(lineText[back:forward])
                    return
                    break
                    return

                back = forward + 1
                num+=1
                
            forward+=1 


    def printItem(self):
        print('''label: {}
xVal: {}
yVal: {}
itemNum: {}\n'''.format(self.label, self.xVal, self.yVal, self.itemNum))
####################################################################
