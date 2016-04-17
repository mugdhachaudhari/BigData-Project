import pandas as pd
import numpy as np
import time

def read_weather_data(file_name):

    file = file_name+'.csv'
    data_frame = pd.read_csv(file)
    try:
        data_frame['Hour'] = data_frame['TimeEST'].map(lambda x: time.strptime(x, "%I:%M %p").tm_hour)
    except:
        data_frame['Hour'] = data_frame['TimeEDT'].map(lambda x: time.strptime(x, "%I:%M %p").tm_hour)
    data_frame['Time'] = data_frame['Hour'].map(lambda x: file_name+str(x).zfill(2))
    data_frame = data_frame[['Time', 'Conditions']]
    try:
        data_frame = data_frame.drop_duplicates(cols='Time')
    except:
        ()
    data_frame = data_frame.set_index('Time')
    return data_frame

year14 = 2014
year15 = 2015

for j in np.arange(1, 13):
    for i in np.arange(1, 32):
        try:
            test_file = str(year14)+str(j).zfill(2)+str(i).zfill(2)
            data_frame = read_weather_data(test_file)
            data_frame.to_csv('cleaned_weather_'+test_file+'.csv', sep=',')
        except:
            continue

        try:
            test_file = str(year15) + str(j).zfill(2) + str(i).zfill(2)
            data_frame = read_weather_data(test_file)
            data_frame.to_csv('cleaned_weather_' + test_file + '.csv', sep=',')
        except:
            continue

print 'done'