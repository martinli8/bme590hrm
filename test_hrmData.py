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
    pass


def test_write_json():
    pass
