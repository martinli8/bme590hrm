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
        corr2csv(a)

    def autocorr(self):
        import numpy as np
        # scaledVoltageData = self.rawData.voltage
        # print(scaledVoltageData)
        # #
        result = np.correlate(self.rawData.voltage, self.rawData.voltage, mode='full')
        return result;

        ## code taken from https://stackoverflow.com/
        #questions/643699/how-can-i-use-numpy-correlate-to-do-autocorrelation/
        #676302

    def corr2csv(self,a):
        df = pd.Dataframe(a,columns = ["column"])
        df.to_csv('list.csv',index = False)
