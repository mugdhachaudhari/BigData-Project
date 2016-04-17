import requests

url = 'http://www.wunderground.com/history/airport/KNYC/{}/{}/{}/DailyHistory.html?req_city=New+York&req_state=NY&req_statename=&reqdb.zip=10106&reqdb.magic=4&reqdb.wmo=99999&format=1'

# Download the data for all 12 month
year14 = 2014
year15 = 2015
for j in range(1, 13):
    for i in range(1, 32):
        r = requests.get(url.format(year14,j, i))
        data = r.text
        f = open('{}{:02}{:02}.csv'.format(year14,j, i), 'wb')
        f.write(data)
        f.close()

        r = requests.get(url.format(year15, j, i))
        data = r.text
        f = open('{}{:02}{:02}.csv'.format(year15, j, i), 'wb')
        f.write(data)
        f.close()