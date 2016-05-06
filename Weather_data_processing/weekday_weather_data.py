import pandas as pd
import numpy as np
import time
import datetime

def read_weather_data():

    file = 'cleaned_weather_2014.csv'
    df = pd.read_csv(file, header=None)
    df.columns = ['Time', 'Condition']
    df['Hour'] = df['Time'].map(lambda x: str(x)[8:10])
    df['Weekday'] = df['Time'].map(lambda x: datetime.datetime(2014,str(x)[4:6],str(x)[6:8]).weekday())
    return df[['Weekday', 'Hour', 'Condition']]

weather_df = read_weather_data()
weather_df.to_csv('weekday_weather_data_2014', sep=',')