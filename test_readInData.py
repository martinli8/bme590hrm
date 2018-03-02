import pytest


def test_faulty_data_load():
    from readData import readData
    myDataset1 = readData("test_data28.csv")
    nanValueTime1 = 0.9
    nanValueVoltage1 = -0.345
    assert myDataset1.time[324] == nanValueTime1
    assert myDataset1.voltage[338] == nanValueVoltage1
    
