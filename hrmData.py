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
        a = self.autocorr()
        # print(a)

    def autocorr(self):
        import numpy as np
        self.rawData.voltage = [x * 1000 for x in self.rawData.voltage]
        # scaledVoltageData = self.rawData.voltage.type
        print(scaledVoltageData)
        #
        # result = np.correlate(self.rawData.voltage, self.rawData.voltage, mode='full')
        # return result[result.size/2:]

        ## code taken from https://stackoverflow.com/
        #questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/
        #676302
