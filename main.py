def main():
    from readData import readData
    from hrmData import hrmData
    from timeSegment import timeSegment
    myDataset = readData("test_data5.csv")
    # myTimePoints = timeSegment(myDataset, 4)
    # print(myTimePoints.segmentList)
    # print(myTimePoints.intervalStart)
    hrmObject = hrmData(myDataset,0,10)
    # print(hrmObject.intervalEnd)
    print(hrmObject.mean_hr_bpm)
    # print(hrmObject.interval)
    # print(hrmObject.rawData.time[324].type)
    # print(myDataset.time[324])
    # print(myDataset.voltage[338])
    # print(myDataset.voltage)


if __name__ == "__main__":
    main()
