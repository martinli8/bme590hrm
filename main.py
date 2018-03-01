def main():
    from readData import readData
    myDataset = readData("test_data30.csv")
    # print(myDataset.time.type())
    if (myDataset.time[965] == "bad data"):
        print("you got got")
    print(myDataset.time[965])
    # print(myDataset.time[965].type())
    # print(myDataset.voltage[338])
    # print(myDataset.voltage)


if __name__ == "__main__":
    main()
