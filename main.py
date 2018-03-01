def main():
    from readData import readData
    myDataset = readData("test_data30.csv")
    # print(myDataset.time.type())
    if (myDataset.time[965] == "bad data"):
        print("you got got")
    print(myDataset.time[965])
    # print(myDataset.time[965].type())
    # print(myDataset.voltage[338])

    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData("test_data3.csv")
    # myTimePoints = timeSegment(myDataset, 4)
    # print(myTimePoints.segmentList)
    # print(myTimePoints.intervalStart)
    hrmObject = hrmData(myDataset, 0, 10)
    print(hrmObject.num_beats)
    # print(hrmObject.voltage_extremes)
    # print(hrmObject.interval)
    # print(hrmObject.rawData.time[324].type)
    # print(myDataset.time[324])
    # print(myDataset.voltage[338])

    myDataset = readData("test_data31.csv")
    print(myDataset.time[38])


if __name__ == "__main__":
    main()
