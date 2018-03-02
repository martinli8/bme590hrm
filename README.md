# bme590hrm

Heart Rate Monitor Assignment from BME590

## Introduction

The premise behind this assignment is to offer a signal processing method for input heart rate monior data (ECG data). There are a few functional specifications that the code is supposed to handle and output. Data is read in from the form of a CSV, and various parameters are determined, including the following: 

- mean_hr_bpm: estimated average heart rate over a user specified interval
- voltage_extremes: max and min detected voltage values on the tuple
- duration: time duration of the sample
- num_beats: the number of detected beats in the strip
- beats: numpy array of the times where a beat was detected

## Code Introduction

The code is separated into four different files, 3 different classes and a main method: 

- readData.py, a class that reads in the CSV file and saves voltage and time attributes
- timeSegment.py, a class that segments the data based on a default time segmentation method (2 second bins)
- hrmData.py, a class that contains the calculated info regarding the input ECG data
- main.py, a script that will execute the necessary steps to extract the relevant information and output the data in a json
- Various unit tests are also included to ensure the code works as intended

## readData.py

Input file format must be a csv, with two columns, the first column being the Time column and the second column being the voltage column. If these parameters are changed for whatever reason, these values can be changed in the data. If numerical values are missing or are instead strings, the class will adjust and interpolate the missing data, however, no more than one adjacent "bad value" can exist. 

## timeSegment.py

This takes in the readData class and segments the voltages accordingly into a list of lists, each list spanning a duration of X seconds (default 2 seconds), and returns it. 

## hrmData.py

This calculates various endpoints. To create the corresponding attributes, it takes in the readData class and an optional start interval and end interval to determine the mean heart rate across that interval. However, a few limitations are in place: the start and end interval times are in seconds, and must be whole integer multiples of the time segmentation (2 seconnds). Time segmentation must also be an integer. 

## main.py

The bread and butter that makes the whole process a lot less painful. Simply run the main method, change the parameters desired (start interval, end interval, input csv file name), and a json file with the same name as the csv file with the output parameters resuts.

# Software bugs and things that can be improved

Currently the heart rate determination is bugged, as the heartrate determination only autocorrelates the entire signal with the entire signal, and finds the time it takes for the time lag, which calculates the heart rate. The desired outcome of the code is that it actually correlates each bin with itself, (line 183 with hrmData.py, as np.argmax(data) should be np.argmax(i). A peak detection method is necessary for the implementation of finding the heart rates across each bin (key if the heart rate increases or decreases during the sampling time). 

In addition, due to the lack of a robust peak detection method, the determination of the number of heart rates and times at which heart rates occur are very rough estimates, and are determined purely from an algebraic standpoint given the duration of the sample and a mean heart rate across the entirety of the sample. 

Try and excepts are also not implemented, although they were chosen not to be implemented, since the callee already has exception raising, and the callers do not anticipate anything to go wrong in the code itself. Given the user input options, the error raising already exists to handle those cases. 

Also one of the unit tests is currently marked as Xfail- comparing the output json data to the input json data. This is due to the floating point precision, and some output values are output as 0.78000000002 instead of 0.78, and a pytest.approx() equivalent comparison was difficult to achieve such that == could successfully pass. 







MIT License

Copyright (c) [2018] [Martin Li]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
