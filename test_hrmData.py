import pytest


def test_subtractDCOffset():
    from hrmData import hrmData
    from readData import readData
    from timeSegment import timeSegment
    myDataset = readData("test_data31.csv")
    hrmObject = hrmData(myDataset)
    subtractedOffsetValues = [-0.027071875, -0.002071875, 0.029178125
                              ,0.054178125, 0.079178125]
    assert hrmObject.meanSubtractedVoltage[0:5] == pytest.approx(subtractedOffsetValues)
