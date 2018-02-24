class readData():

    def __init__(self,csvFileName):
        self.csvFileName = csvFileName
        self.time = None
        self.voltage = None
        self.columnTime = 1
        self.columnVoltage = 2
        # self.checkTimeNan()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,time):
        import pandas as pd
        timeList = []
        timeCol = pd.read_csv(self.csvFileName, header=None, usecols=[0])
        for row in timeCol.values:
            timeList.append(row[0])
        self.__time = timeList
        self.checkTimeNaN()

    def checkTimeNaN(self):
        import numpy as np
        a = np.empty(1)
        a[:] = np.nan
        for i,rows in enumerate(self.__time):
            if (str(self.__time[i]) == str(a[0])):
                self.__time[i] = (self.__time[i-1] + self.__time[i+1])/2

    @property
    def voltage(self):
        return self.__voltage

    @voltage.setter
    def voltage(self,voltage):
        import pandas as pd
        voltageCol = pd.read_csv(self.csvFileName, header=None, usecols=[1])
        self.__voltage = voltageCol
