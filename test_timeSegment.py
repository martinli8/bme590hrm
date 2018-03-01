import pytest


def test_time_index():
    timesAt2SecondsFile2 = [720, 1440, 2160, 2880, 3600, 4320,
                            5040, 5760, 6480, 7200, 7920, 8640, 9360]
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData("test_data2.csv")
    myTimePoints = timeSegment(myDataset, 2)
    assert myTimePoints.listOfSegmentsIdx == timesAt2SecondsFile2


def test_voltage_list():
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData('easytestfile.csv')
    myTimePoints = timeSegment(myDataset, 4)
    expectedVoltageValues = [[100, 101, 102, 103], [104, 105, 106, 107],
                             [108, 109, 110, 111], [112, 113, 114, 115],
                             [116, 117, 118, 119]]
    assert myTimePoints.segmentList == expectedVoltageValues


def test_default_value_for_time_segment():
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData('easytestfile.csv')
    myTimePoints = timeSegment(myDataset)
    expectedVoltageValues = [[100, 101], [102, 103], [104, 105], [106, 107], [
        108, 109], [110, 111], [112, 113], [114, 115], [116, 117], [118, 119]]
    assert myTimePoints.segmentList == expectedVoltageValues
