import requests

url = 'https://storage.googleapis.com/tlc-trip-data/{}/{}_tripdata_{}-{}.csv'
# https://storage.googleapis.com/tlc-trip-data/2015/yellow_tripdata_2015-01.csv
# url = 'http://www.wunderground.com/history/airport/KNYC/{}/{}/{}/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=&reqdb.zip=10106&reqdb.magic=4&reqdb.wmo=99999&format=1'
# Download the data for all 12 month
year14 = 2014
year15 = 2015


for j in range(1, 13):
    i = "%02d" % j

    r = requests.get(url.format(year14,'yellow', year14, i), stream = True)
    with open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('yellow', year14,i), 'wb') as f:
    # data = r.text
    # print data
    # f = open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('yellow', year14,i), 'wb')

        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    f.close()

    r = requests.get(url.format(year14, 'green', year14, i), stream=True)
    with open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('green', year14, i), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    f.close()

    r = requests.get(url.format(year15, 'green', year15, i), stream=True)
    with open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('green', year15, i), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    f.close()

    r = requests.get(url.format(year15, 'yellow', year15, i), stream=True)
    with open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('yellow', year15, i), 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    f.close()

    # r = requests.get(url.format(year15,'yellow', year15, i))
    # data = r.text
    # # print data
    # f = open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('yellow', year15,i), 'wb')
    # f.write(data)
    # f.close()
    #
    # r = requests.get(url.format(year14,'green', year14, i))
    # data = r.text
    # # print data
    # f = open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('green', year14,i), 'wb')
    # f.write(data)
    # f.close()
    #
    # r = requests.get(url.format(year15,'green', year15, i))
    # data = r.text
    # # print data
    # f = open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('green', year15,i), 'wb')
    # f.write(data)
    # f.close()
    #
    # r = requests.get(url.format(year15, 'green', year15, i))
    # data = r.text
    # # print data
    # f = open('YellowGreenData/{}_{}_{}_tripdata.csv'.format('green', year15, i), 'wb')
    # f.write(data)
    # f.close()
