import pytest


def test_subtractDCOffset():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    subtractedOffsetValues = [-0.027071875, -0.002071875, 0.029178125,
                              0.054178125, 0.079178125]
    assert hrmObject.meanSubtractedVoltage[0:5] == pytest.approx(subtractedOffsetValues)


def test_determineLagTime():
    pass


def test_intervalHR():
    pass


def test_convertTimeToIdx():
    pass


def test_voltage_extremes():
    pass


def test_num_beats():
    pass


def test_time_of_beats():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    locationOfBeats = [0.,     0.7715, 1.543,  2.3145, 3.086, 3.8575, 4.629, 5.4005, 6.172,
                       6.9435, 7.715,  8.4865, 9.258, 10.0295, 10.801,  11.5725, 12.344, 13.1155,
                       13.887]
    assert locationOfBeats == pytest.approx(hrmObject.beats)


def test_write_json():
    pass
