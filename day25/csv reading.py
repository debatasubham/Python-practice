#with open ("C:\python\day25\weather_data.csv") as data_file:
#data = data_file.readlines()
#print(data)
        

import csv

with open(r"C:\python\day25\weather_data.csv", encoding="utf-8-sig") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        if len(row) > 1 and row[1] != "temp":
            temperatures.append(int(row[1]))
    print(temperatures)

