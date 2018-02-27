class hrmData():

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
        import numpy as np
        import matplotlib.pyplot as plt

        meanSubtractedVoltage = []
        meanVal = np.mean(self.rawData.voltage)
        meanSubtractedVoltage[:] = [x - meanVal for x in self.rawData.voltage]
        self.adjVol = self.smoothVoltage(meanSubtractedVoltage)
        autoCorrelationData = self.autocorr(meanSubtractedVoltage)
        lagTimes = self.determineLagTime(autoCorrelationData)
        # print(lagTimes)
        self.intervalHR(lagTimes)
        self.visualizeData(autoCorrelationData)

    def smoothVoltage(self, data):
        from scipy.signal import savgol_filter
        import matplotlib.pyplot as plt
        import warnings
        warnings.filterwarnings(action="ignore", module="scipy",
                                message="^internal gelsd")
        return savgol_filter(data, 11, 5)

    def autocorr(self, data):
        import numpy as np
        import math
        firstNValuesToSkip = 14
        result = np.correlate(data, data, mode='same')
        result = result[math.ceil(len(result)/2):]
        result = result[firstNValuesToSkip:]
        return result

        # code taken from https://stackoverflow.com/
        # questions/643699/how-can-i-use-numpy-
        # correlate-to-do-autocorrelation/676302

    def determineLagTime(self, data):
        heartRateList = []
        import numpy as np
        import math
        from timeSegment import timeSegment

        mySplitVoltages = timeSegment(self.rawData)
        # print(mySplitVoltages.segmentList)

        # if self.intervalStart == None:
        #     ind = np.argmax(data) + 14;
        #     trueInd = ind - 14;
        #     mymax = np.amax(data)
        #     timeAtMax = self.rawData.time[trueInd]
        #     print(timeAtMax)
        #     heartRateOverAllTime = 60/timeAtMax
        #     self.__mean_hr_bpm = heartRateOverAllTime

        # print(heartRateOverAllTime)
        # print(timeAtMax)

        # else:
        for i in mySplitVoltages.segmentList:
            ind = np.argmax(data) + 14
            trueInd = ind - 14
            mymax = np.amax(data)
            timeAtMax = self.rawData.time[trueInd]
            heartRateOverAllTime = 60/timeAtMax
            heartRateList.append(heartRateOverAllTime)
        # print(heartRateList)
        return heartRateList


    def intervalHR(self,lagTimes):
        import numpy as np
        startIdx = self.convertTimeToIdx(self.intervalStart)
        endIdx = self.convertTimeToIdx(self.intervalEnd)
        self.__mean_hr_bpm = np.mean(lagTimes[startIdx:endIdx])


    def convertTimeToIdx(self,time):
        import math
        idx = math.floor(math.floor(time)/self.timeSegment)
        return idx


    def visualizeData(self, a):
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.DataFrame(a)
        df.to_csv('list.csv', index=False, header=False)
        plt.plot(a)
        plt.show()
