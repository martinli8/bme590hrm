import pytest


def test_faulty_data_load():
    from readData import readData
    myDataset1 = readData("test_data28.csv")
    nanValueTime1 = 0.9
    nanValueVoltage1 = -0.345
    assert myDataset1.time[324] == nanValueTime1
    assert myDataset1.voltage[338] == nanValueVoltage1
    myDataset2 = readData("test_data30.csv")

    badDataTime = 3.86
    badDataVoltage = -0.025
    assert myDataset2.time[965] == badDataTime
    assert myDataset2.voltage[972] == badDataVoltage


def test_regular_data_read():
    from readData import readData
    myDataset1 = readData("test_data3shortTime.csv")
    timeFromCSV = [0, 0.003, 0.006, 0.008, 0.011, 0.014, 0.017, 0.019, 0.022,
                   0.025, 0.028, 0.031, 0.033, 0.036, 0.039, 0.042, 0.044,
                   0.047, 0.05, 0.053]
    assert pytest.approx(myDataset1.time[0:20]) == timeFromCSV


def test_checkOutOfRange():
    from readData import readData
    import warnings
    with pytest.warns(UserWarning):
        myDataset1 = readData("test_data32.csv")
        warnings.warn("outside of normal ECG range!", UserWarning)
