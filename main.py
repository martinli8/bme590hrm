def main():
    from readData import readData
    from hrmData import hrmData
    myDataset = readData("test_data2.csv")
    hrmObject = hrmData(myDataset)
    print(hrmObject.mean_hr_bpm)
    # print(hrmObject.interval)
    # print(hrmObject.rawData.time[324].type)
    # print(myDataset.time[324])
    # print(myDataset.voltage[338])
    # print(myDataset.voltage)


if __name__ == "__main__":
    main()
