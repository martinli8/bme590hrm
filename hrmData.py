class hrmData():

    """This is a hrmData class. It calculates various endpoints regarding the
    input heartrate monitor data

    Attributes:
        :rawData (readData): readData class that contains time and voltage

        :intervalStart (int): the beginning time to calculate the
        mean heartrate, if no value specified, starts at beginning of data, or
        time = 0, must be a multiple of timeSegment

        :intervalEnd (int): the ending time to calculate the mean heartrate,
        if no value specified, this value is the last possible time, must be
        a multiple of timeSegment

        :timeSegment (int): the seconds value to create binning for determining
        the heart rate, Default value is 2, for example, if 4 is specified,
        data is split up into 4 second bins

        :mean_hr_bpm (float): the mean heartrate across the specified time
        interval

        :voltage extremes (tuple): the values of the highest and lowest
         voltages detected

        :duration (float): the time duration that the data spans over

        :num_beats (float): estimated number of beats determined by the mean
        heart rate instead of actually peak detecting

        :beats (list): times at which beats occur, estimated by calculating the
        average heart rate across a certain time and guessing that a heartbeat
        occurs accordingly at that time

        :adjVol (list): a smoothed list of the voltages (original voltages
        put through a SavGol Filter)

        """

    def __init__(self, readDataClass, intervalStart=None, intervalEnd=None):

        self.rawData = readDataClass
        self.intervalStart = intervalStart if intervalStart is not None else 0
        self.intervalEnd = intervalEnd if intervalEnd is not None  \
            else self.rawData.time[-1]
        self.timeSegment = 2
        self.mean_hr_bpm = None
        self.voltage_extremes = None
        self.duration = self.rawData.time[-1]
        self.num_beats = None
        self.beats = None
        self.adjVol = None

    @property
    def mean_hr_bpm(self):
        return self.__mean_hr_bpm

    @mean_hr_bpm.setter
    def mean_hr_bpm(self, mean_hr_bpm):
        """
        Finds the mean heart rate over a certain time interval

        A few steps are taken, first the voltages have the DC offset subtracted
        which is done by subtracting the mean across the entire signal.
        The signal is then smoothed, and autocorrelated with individual bins
        with the lag time then determined to piece together
        the heart rate over that certain bin (time period).

        :param self: hrmData Object
        :returns: mean_hr_bpm attribute
        """

        self.meanSubtractedVoltage = self.subtractDCOffset()
        self.adjVol = self.smoothVoltage(self.meanSubtractedVoltage)
        autoCorrelationData = self.autocorr(self.meanSubtractedVoltage)
        lagTimes = self.determineLagTime(autoCorrelationData)
        self.intervalHR(lagTimes)
        self.visualizeData(autoCorrelationData)

    def subtractDCOffset(self):
        """
        Subtracts the DC offset by taking the mean of the entire signal.

        :param self: hrmData Object
        :returns: list of voltage values, mean subtracted
        """

        import numpy as np
        meanSubtractedVoltage = []
        meanVal = np.mean(self.rawData.voltage)
        # print(meanVal)
        meanSubtractedVoltage[:] = [x - meanVal for x in self.rawData.voltage]
        # print(meanSubtractedVoltage)
        return meanSubtractedVoltage

    def smoothVoltage(self, data):
        """
        Smooths the signal by applying a Savitsky Golay filter

        :param self: hrmData Object
        :param data: voltage with DC subtracted
        :returns: list of voltage values, filter applied
        """

        from scipy.signal import savgol_filter
        import matplotlib.pyplot as plt
        import warnings
        warnings.filterwarnings(action="ignore", module="scipy",
                                message="^internal gelsd")
        return savgol_filter(data, 11, 5)

    def autocorr(self, data):
        """
        Autocorrelates each individual bin with itself using mode = 'same'

        :param self: hrmData Object
        :param data: smoothed data
        :returns: autocorrelation data
        """

        import numpy as np
        import math
        firstNValuesToSkip = 14
        result = np.correlate(data, data, mode='same')
        result = result[math.ceil(len(result)/2):]
        result = result[firstNValuesToSkip:]
        return result

    def determineLagTime(self, data):
        """
        Determines the lag time for each bin

        Skips the first few values to account for the first point being the
        best match, and looks for the next peak, assumes the max value is the
        next peak and thus establishes the time delay. Inverse is taken for
        frequency of heartrate.

        :param self: hrmData Object
        :param data: autocorrelation data
        :returns: list of heart rates(HR at each bin)
        """

        heartRateList = []
        import numpy as np
        import math
        from timeSegment import timeSegment
        mySplitVoltages = timeSegment(self.rawData)
        firstNValuesToSkip = 14

        for i in mySplitVoltages.segmentList:
            ind = np.argmax(data)
            trueInd = ind - firstNValuesToSkip
            mymax = np.amax(data)
            timeAtMax = self.rawData.time[trueInd]
            heartRateOverAllTime = 60/timeAtMax
            heartRateList.append(heartRateOverAllTime)
        return heartRateList

    def intervalHR(self, lagTimes):
        """
        Determines the mean HR over specified interval

        :param self: hrmData Object
        :param lagTimes: List of heart rates(HR at each bin)
        :returns: heart rate over specified interval
        """

        import numpy as np
        startIdx = self.convertTimeToIdx(self.intervalStart)
        endIdx = self.convertTimeToIdx(self.intervalEnd)
        self.__mean_hr_bpm = np.mean(lagTimes[startIdx:endIdx])

    def convertTimeToIdx(self, time):
        """
        Helper method to convert time interval to actual time index

        :param self: hrmData Object
        :param time: Specified time to convert to index
        :returns: Index of the time
        """

        import math
        idx = math.floor(math.floor(time)/self.timeSegment)
        return idx

    def visualizeData(self, data):
        """
        If data is to be visualized, this does it

        :param self: hrmData hrmObject
        :param data: Voltages to visualize
        """
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.DataFrame(data)
        df.to_csv('list.csv', index=False, header=False)
        # plt.plot(a)
        # plt.show()

    @property
    def voltage_extremes(self):
        return self.__voltage_extremes

    @voltage_extremes.setter
    def voltage_extremes(self, voltage_extremes):
        """Finds the voltage extremes

        :param self: hrmData Object
        :returns: voltage_extremes attribute as a Tuple
        """

        import numpy as np
        maxValue = np.amax(self.rawData.voltage)
        minValue = np.amin(self.rawData.voltage)
        maxMinTuple = (maxValue, minValue)
        self.__voltage_extremes = maxMinTuple

    @property
    def num_beats(self):
        return self.__num_beats

    @num_beats.setter
    def num_beats(self, num_beats):
        """Guesses the number of beats that occur during the data by dividing
        the heart rate and the time accordingly

        :param self: hrmData Object
        :returns: number of beats that occur (ROUGH ESTIMATE)
        """

        print(self.duration)
        print(self.mean_hr_bpm)
        self.__num_beats = self.duration/60*(self.mean_hr_bpm)
