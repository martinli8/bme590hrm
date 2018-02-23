class readData():

    def __init__(self,csvFileName):
        self.csvFileName = csvFileName
        self.time = None
        self.voltage = None
        self.columnTime = 1
        self.columnVoltage = 2
        self.checkTimeNan()

    @property
    def time(self):
        return self.__time

    @time.setter
    def time(self,time):
        import pandas as pd
        timeCol = pd.read_csv(self.csvFileName, header=None, usecols=[0])
        self.__time = timeCol
        self.checkTimeNaN()

    def checkTimeNaN(self):
        for 

    @property
    def voltage(self):
        return self.__voltage

    @voltage.setter
    def voltage(self,voltage):
        import pandas as pd
        voltageCol = pd.read_csv(self.csvFileName, header=None, usecols=[1])
        self.__voltage = voltageCol
