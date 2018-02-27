class hrmData():

    def __init__(self,readDataClass,intervalStart = None,intervalEnd = None):

        self.rawData = readDataClass

        self.intervalStart = intervalStart
        self.intervalEnd = intervalEnd
        self.timeSegment = 2;

        self.mean_hr_bpm = None
        self.voltage_extremes = None
        self.duration = None
        self.num_beats = None
        self.beats = None
        self.adjVol = None


    @property
    def mean_hr_bpm(self):
        return self.__mean_hr_bpm

    @mean_hr_bpm.setter
    def mean_hr_bpm(self,mean_hr_bpm):
        import numpy as np
        import matplotlib.pyplot as plt
        meanVal = np.mean(self.rawData.voltage)
        self.rawData.voltage[:] = [ x - meanVal for x in self.rawData.voltage]
        self.adjVol = self.smoothVoltage(self.rawData.voltage)
        autoCorrelationData = self.autocorr(self.rawData.voltage)
        lagTime = self.determineLagTime(autoCorrelationData)
        self.visualizeData(autoCorrelationData)


    def smoothVoltage(self,data):
        from scipy.signal import savgol_filter
        import matplotlib.pyplot as plt
        import warnings
        warnings.filterwarnings(action="ignore", module="scipy", \
            message="^internal gelsd")
        return savgol_filter(data,11,5)

    def autocorr(self,data):
        import numpy as np
        import math
        firstNValuesToSkip = 10;
        result = np.correlate(data, data, mode='same')
        result = result[math.ceil(len(result)/2):]
        result = result[firstNValuesToSkip:]
        return result;

        ## code taken from https://stackoverflow.com/
        #questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/
        #676302

    def determineLagTime(self,data):
        heartRateList = []
        import numpy as np
        import math
        if self.intervalStart == None:
            ind = np.argmax(data) + 10;
            trueInd = ind - 10;
            mymax = np.amax(data)
            timeAtMax = self.rawData.time[trueInd]
            heartRateOverAllTime = 60/timeAtMax
            self.__mean_hr_bpm = heartRateOverAllTime

            print(heartRateOverAllTime)
            print(timeAtMax)

        else:

            self.__mean_hr_bpm = 20


    def visualizeData(self,a):
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.DataFrame(a)
        df.to_csv('list.csv',index = False,header = False)
        plt.plot(a)
        # plt.show()
