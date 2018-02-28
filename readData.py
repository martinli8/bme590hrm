class readData():
    """This is a readData class. It stores the data read in from the CSV.

    Attributes:
        :csvFileName (string): String with the CSV File name that is read in

        :time (list): list of the times read in from the CSV

        :voltage (list): list of the voltages read in from the CSV

        :columnTime (int): The column where the time is located in the CSV

        :columnVoltage (int): The column where the voltage is placed in the CSV

    """

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
        """
        Sets the time attribute by reading in the values, appending to a list,
        checking for NaNs and interpolates accordingly, and returns the list.

        :param self: readData class
        :returns: the time as an attribute to the readData Class
        """

        import pandas as pd
        timeList = []
        timeCol = pd.read_csv(self.csvFileName, header=None, usecols=[0])
        for row in timeCol.values:
            timeList.append(row[0])
        self.__time = timeList
        self.checkTimeNaN()

    def checkTimeNaN(self):
        """
        Corrects any "NaN"s or blanks in the actual data when read in

        :param self: readData class
        :returns: the time in the ReadData Class, Nans corrected
        """

        import numpy as np
        a = np.empty(1)
        a[:] = np.nan
        for i, rows in enumerate(self.__time):
            if (str(self.__time[i]) == str(a[0])):
                self.__time[i] = (self.__time[i-1] + self.__time[i+1])/2
    @property
    def voltage(self):
        return self.__voltage

    @voltage.setter
    def voltage(self, voltage):
        """
        Sets the voltage attribute by reading in the values,
        appending to a list, checking for NaNs and values out of Range,
        and returns the list.

        :param self: readData class
        :returns: the voltage as an attribute to the readData Class
        """

        import pandas as pd
        voltList = []
        voltageCol = pd.read_csv(self.csvFileName, header=None, usecols=[1])
        for row in voltageCol.values:
            voltList.append(row[0])
        self.__voltage = voltList
        self.checkVoltageNan()
        self.checkOutOfECGRange()

    def checkVoltageNan(self):
        """
        Corrects any "NaN"s or blanks in the actual data when read in

        :param self: readData class
        :returns: the time in the ReadData Class, Nans corrected
        """

        import numpy as np
        b = np.empty(1)
        b[:] = np.nan
        for i, rows in enumerate(self.__voltage):
            if (str(self.__voltage[i]) == str(b[0])):
                self.__voltage[i] = (
                    self.__voltage[i-1] + self.__voltage[i+1])/2

    def checkOutOfECGRange(self):
        """
        Checks for any values out of the 300mV ecg range

        :param self: readData class
        :returns: A warning if value is outside range
        """

        import warnings
        import numpy as np
        import logging
        voltageThreshold = 300
        outsideRange = [i for i in self.__voltage if (i >= voltageThreshold)]
        if len(outsideRange) > 0:
            warnings.warn("outside of normal ECG range!", UserWarning)
