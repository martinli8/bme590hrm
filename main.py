def main():
    from readData import readData
    from hrmData import hrmData
    import numpy as np
    import json
    csvFileName = "test_data31.csv"
    myDataset = readData(csvFileName)
    hrmObject = hrmData(myDataset)
    write_to_json(csvFileName, hrmObject)
    # with open('test_data31.json') as data_file:
    #     data_loaded = json.load(data_file)
    #     print(data_loaded.type)

def write_to_json(csvFileName, hrmDataClass):
    """ This method writes to a json file.

    :param csvFileName: Takes in the name of the csv file to change to a json
    :param hrmDataClass: Takes in the class with the attributes to save to json
    :returns: Json file with same name as the original csv file with attributes

    """

    import pandas as pd
    jsonFileName = csvFileName.rstrip('csv')
    jsonFileName = jsonFileName + 'json'
    print(jsonFileName)
    mean_hr_bpm = hrmDataClass.mean_hr_bpm
    voltage_extremes = hrmDataClass.voltage_extremes
    duration = hrmDataClass.duration
    num_beats = hrmDataClass.num_beats
    beats = hrmDataClass.beats.tolist()

    data = {'File Name': csvFileName,
            'mean_hr_bpm': mean_hr_bpm,
            'voltage_extremes': voltage_extremes,
            'duration': duration,
            'num_beats': num_beats,
            'beats': beats}

    import json
    with open(jsonFileName, 'w') as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
