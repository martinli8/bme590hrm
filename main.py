def main():
    from readData import readData
    myDataset = readData("test_data28.csv")
    print(myDataset.time[324])
    print(myDataset.voltage[338])
    # print(myDataset.voltage)


if __name__ == "__main__":
    main()
