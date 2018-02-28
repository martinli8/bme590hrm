def main():
    from readData import readData
    myDataset = readData("test_data31.csv")
    print(myDataset.time[38])
    print(myDataset.voltage[338])
    # print(myDataset.voltage)


if __name__ == "__main__":
    main()
