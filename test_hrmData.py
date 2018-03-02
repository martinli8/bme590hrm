import pytest


def test_subtractDCOffset():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    subtractedOffsetValues = [-0.027071875, -0.002071875, 0.029178125,
                              0.054178125, 0.079178125]
    assert hrmObject.meanSubtractedVoltage[0:5] == \
        pytest.approx(subtractedOffsetValues)


def test_determineLagTime():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    actualHR = 80
    assert 0.9*actualHR < hrmObject.heartRateList[0] < 1.1*actualHR
    assert 0.9*actualHR < hrmObject.heartRateList[1] < 1.1*actualHR
    assert 0.9*actualHR < hrmObject.heartRateList[2] < 1.1*actualHR
    assert 0.9*actualHR < hrmObject.heartRateList[3] < 1.1*actualHR
    assert 0.9*actualHR < hrmObject.heartRateList[4] < 1.1*actualHR
    assert 0.9*actualHR < hrmObject.heartRateList[5] < 1.1*actualHR


def test_intervalHR():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    actualHR = 84.38818565400844
    assert pytest.approx(hrmObject.global_mean_hr_bpm) == 84.38818565400844

    hrmObject2 = hrmData(myDataset, 2, 8)
    assert pytest.approx(hrmObject.global_mean_hr_bpm) == 84.38818565400844


def test_convertTimeToIdx():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    startIdx1 = 0
    endIdx1 = 6
    assert startIdx1 == hrmObject.startIdx
    assert endIdx1 == hrmObject.endIdx

    hrmObject2 = hrmData(myDataset, 2, 8)
    startIdx2 = 1
    endIdx2 = 4
    assert startIdx2 == hrmObject2.startIdx
    assert endIdx2 == hrmObject2.endIdx


def test_voltage_extremes():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    maxMinValue = (0.7875, -0.19375)
    assert pytest.approx(hrmObject.voltage_extremes) == maxMinValue


def test_num_beats():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    numBeatsin31 = 19
    assert numBeatsin31*0.8 < hrmObject.num_beats < numBeatsin31*1.2


def test_time_of_beats():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    locationOfBeats = [0., 0.7715, 1.543,  2.3145, 3.086, 3.8575, 4.629,
                       5.4005, 6.172, 6.9435, 7.715,  8.4865, 9.258, 10.0295,
                       10.801,  11.5725, 12.344, 13.1155, 13.887]
    assert locationOfBeats == pytest.approx(hrmObject.beats)


@pytest.mark.xfail
def test_write_json():
    from main import main
    from hrmData import hrmData
    from readData import readData
    import json
    import unittest
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    main()
    data = {'File Name': hrmObject.rawData.csvFileName,
            'mean_hr_bpm': hrmObject.mean_hr_bpm,
            'voltage_extremes': hrmObject.voltage_extremes,
            'duration': hrmObject.duration,
            'num_beats': hrmObject.num_beats,
            'beats': hrmObject.beats}
    with open('test_data31.json') as data_file:
        data_loaded = json.load(data_file)
    data_loaded_list = data_loaded.items()
    data_list = data.items()
    assert data_loaded_list == data_list
