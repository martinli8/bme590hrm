class readData():

    def __init__(self,csvFileName):
        self.csvFileName = None
        self.time = None
        self.voltage = None
        self.columnTime = 1
        self.columnVoltage = 2

    @property
    def time(self):
        return self.__time
    # def voltage(self):
    #     return self.__voltage

    @time.setter
    def time(self,time):
        import pandas as pd
        reader = pd.read_csv(file, header=None)
        time = reader.values[1]
