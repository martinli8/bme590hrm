def main():
    from readData import readData
    from hrmData import hrmData

    csvFileName = "test_data32.csv"
    myDataset = readData(csvFileName)
    # print(myDataset.voltage)
    hrmObject = hrmData(myDataset)
    print(hrmObject.mean_hr_bpm)
    # print(hrmObject.meanSubtractedVoltage[0:5])
    # print(hrmObject.beats)
    # print(myDataset.time[324])
    # print(myDataset.voltage[338])
    # print(myDataset.voltage)

    # write_to_json(csvFileName,hrmObject)


def write_to_json(csvFileName,hrmDataClass):
    import pandas as pd
    jsonFileName = csvFileName.rstrip('csv')
    jsonFileName = jsonFile.append('json')
    print(jsonFileName)
    mean_hr_bpm = hrmDataClass.mean_hr_bpm
    voltage_extremes = hrmDataClass.voltage_extremes
    duration = hrmDataClass.duration
    num_beats = hrmDataClass.num_beats
    beats = hrmDataClass.beats.tolist()

    data =            { 'File Name'        : jsonFileName,
                        'mean_hr_bpm'      : mean_hr_bpm ,
                        'voltage_extremes' : voltage_extremes,
                        'duration'         : duration,
                        'num_beats'        : num_beats,
                        'beats'            : beats  }
    #
    # import json
    # with open(jsonFileName, 'w') as outfile:
    #     json.dump(data,outfile)

if __name__ == "__main__":
    main()
