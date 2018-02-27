class timeSegment():

    DEFAULT_intervalStart = 0

    def __init__(self, readDataClass, timeSegment=None):

        self.rawData = readDataClass
        self.timeSegment = timeSegment if timeSegment is not None else 2
        self.listOfSegmentsIdx = None
        self.segmentList = None

    @property
    def listOfSegmentsIdx(self):
        return self.__listOfSegmentsIdx

    @listOfSegmentsIdx.setter
    def listOfSegmentsIdx(self, listOfSegmentsIdx):
        self.determineTimeIndices()

    def determineTimeIndices(self):
        import math
        import numpy as np
        time = self.rawData.time
        timeValueToMatch = self.timeSegment
        lastTimePoint = time[-1]
        lastSegmentTP = math.floor(math.floor(lastTimePoint)/self.timeSegment)*self.timeSegment
        print(lastSegmentTP)

        indexListOfMatch = []

        while timeValueToMatch <= lastSegmentTP:

            index = (np.abs(np.asarray(time)-timeValueToMatch)).argmin()
            indexListOfMatch.append(index)
            timeValueToMatch = timeValueToMatch + self.timeSegment

        self.__listOfSegmentsIdx = indexListOfMatch

    @property
    def segmentList(self):
        return self.__segmentList

    @segmentList.setter
    def segmentList(self, segmentList):
        self.determineSegments()

    def determineSegments(self):
        mySegmentList = [[] for _ in range(len(self.listOfSegmentsIdx))]
        voltage = self.rawData.voltage
        beginningValue = 0
        nextValue = self.listOfSegmentsIdx[0]
        voltListToAdd = voltage[beginningValue:nextValue]
        mySegmentList[0].append(voltListToAdd)

        for counter in range(0, (len(self.listOfSegmentsIdx)-1)):
            beginningValue = nextValue
            nextValue = self.listOfSegmentsIdx[counter+1]
            voltListToAdd2 = voltage[beginningValue:nextValue]
            mySegmentList[counter+1].append(voltListToAdd2)

        flatList = []
        for x in mySegmentList:
            for y in x:
                flatList.append(y)

            self.__segmentList = flatList
