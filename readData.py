class readData():

    def __init__(self, csvFileName):
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
    def time(self, time):
        import pandas as pd
        timeList = []
        timeCol = pd.read_csv(self.csvFileName, header=None, usecols=[0])
        for row in timeCol.values:
            timeList.append(row[0])
        self.__time = timeList
        self.checkTimeNaN()
        self.convert_to_native_python_dtype()

    def checkTimeNaN(self):
        import numpy as np
        a = np.empty(1)
        a[:] = np.nan
        for i, rows in enumerate(self.__time):
            if (str(self.__time[i]) == str(a[0])):
                self.__time[i] = (self.__time[i-1] + self.__time[i+1])/2

    def convert_to_native_python_dtype(self):
        import numpy
        regularList = [];
        for i in self.__time:
            regularList.append(numpy.asscalar(i))
        self.__time = regularList

    @property
    def voltage(self):
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage):
        import pandas as pd
        voltList = []
        voltageCol = pd.read_csv(self.csvFileName, header=None, usecols=[1])
        for row in voltageCol.values:
            voltList.append(row[0])
        self.__voltage = voltList
        self.checkVoltageNan()

    def checkVoltageNan(self):
        import numpy as np
        b = np.empty(1)
        b[:] = np.nan
        for i, rows in enumerate(self.__voltage):
            if (str(self.__voltage[i]) == str(b[0])):
                self.__voltage[i] = (
                    self.__voltage[i-1] + self.__voltage[i+1])/2
    #
    # def convertToList(self):
    #     regularList = [];
    #     for
