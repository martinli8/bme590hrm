import logging


class timeSegment():

    """This is a timeSegment class.

    Attributes:
        :rawData (readData): readData class that contains time and voltage

        :timeSegment (integer): number of seconds to split data segments into

        :listOfSegmentsIdx (list): list of time indices that data is split into

        :segmentList (list): list of list of voltages that are split up into
        segments

    """

    def __init__(self, readDataClass, timeSegment=None):

        self.rawData = readDataClass
        self.timeSegment = timeSegment if timeSegment is not None else 2
        logging.debug("The time segment bins are %f seconds long",
                      self.timeSegment)
        self.listOfSegmentsIdx = None
        self.segmentList = None

    @property
    def listOfSegmentsIdx(self):
        return self.__listOfSegmentsIdx

    @listOfSegmentsIdx.setter
    def listOfSegmentsIdx(self, listOfSegmentsIdx):
        """
        Finds the time index for each segment of X seconds

        :param self: timeSegment Object
        :returns: listOfSegmentsIdx attribute
        """

        self.determineTimeIndices()

    def determineTimeIndices(self):
        """
        Finds the time index for each segment of X seconds

        :param self: timeSegment Object
        :returns: listOfSegmentsIdx attribute
        """

        import math
        import numpy as np
        time = self.rawData.time
        timeValueToMatch = self.timeSegment
        lastTimePoint = time[-1]
        logging.info("Last time point is %d ", lastTimePoint)
        lastSegmentTP = math.floor(
            math.floor(
                lastTimePoint)/self.timeSegment)*self.timeSegment

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
        """
        Finds the corresponding voltages for each time segment

        :param self: timeSegment Object, segment List Attributes
        :returns: Segment lists attribute, list of list
        """
        self.determineSegments()

    def determineSegments(self):
        """
        Finds the voltages for each time segment

        :param self: timeSegment Object
        :returns: segmentlists attribute, which is a list of lists
        """
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
