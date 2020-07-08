import time
import os
import pandas
#install pandas: pip3 install pandas
#working on windows using this to specify filepath
here = os.path.dirname(os.path.abspath(__file__))

weather_data = "%s/files/weather_station_data.csv" % (here)

while True:
    if os.path.exists(weather_data):
        data = pandas.read_csv(weather_data)
        print(data.mean())
    else:
        print("File does not eists.")
            
    time.sleep(10)
    break