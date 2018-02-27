import pytest

def test_time_index():
    timesAt2SecondsFile2 = [720, 1440, 2160, 2880, 3600, 4320, \
    5040, 5760, 6480, 7200, 7920, 8640, 9360]
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData("test_data2.csv")
    myTimePoints = timeSegment(myDataset)
    assert myTimePoints.listOfSegmentsIdx == timesAt2SecondsFile2


def test_voltage_list():
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = read('easytestfile.csv')
    myTimePoints = timeSegment(myDataset)
