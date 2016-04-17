import numpy as np

year14 = 2014
year15 = 2015

y14 = open("cleaned_weather_2014.csv","a")
y15 = open("cleaned_weather_2015.csv","a")

# first file:
for line in open("cleaned_weather_20140101.csv"):
    y14.write(line)

for line in open("cleaned_weather_20150101.csv"):
    y15.write(line)
# now the rest:
for j in np.arange(1, 13):
    for i in np.arange(1, 32):
        if(j==1 and i==1):
            continue
        file1 = 'cleaned_weather_'+str(year14)+str(j).zfill(2)+str(i).zfill(2)+'.csv'
        f1 =open(file1)
        f1.next()
        for line in f1:
            y14.write(line)
        f1.close()

        file1 =  'cleaned_weather_'+str(year15) + str(j).zfill(2) + str(i).zfill(2)+'.csv'
        f1 = open(file1)
        f1.next()
        for line in f1:
            y15.write(line)
        f1.close()

y14.close()
y15.close()