class hrmData():

    def __init__(self,readDataClass):
        self.rawData = readDataClass
        self.mean_hr_bpm = None
        self.voltage_extremes = None
        self.duration = None
        self.num_beats = None
        self.beats = None

    @property
    def mean_hr_bpm(self):
        return self.__mean_hr_bpm

    @mean_hr_bpm.setter
    def mean_hr_bpm(self,mean_hr_bpm):
        import numpy as np
        meanVal = np.mean(self.rawData.voltage)
        self.rawData.voltage[:] = [ x - meanVal for x in self.rawData.voltage]
        a = self.autocorr()
        self.corr2csv(a)

    def autocorr(self):
        import numpy as np
        import math
        # scaledVoltageData = self.rawData.voltage
        # print(scaledVoltageData)
        # #
        result = np.correlate(self.rawData.voltage, self.rawData.voltage, mode='same')
        result = result[math.ceil(len(result)/2):]
        return result;

        ## code taken from https://stackoverflow.com/
        #questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/
        #676302

    def corr2csv(self,a):
        import matplotlib.pyplot as plt
        import pandas as pd
        df = pd.DataFrame(a)
        df.to_csv('list.csv',index = False,header = False)
        plt.plot(a)
        plt.show()
