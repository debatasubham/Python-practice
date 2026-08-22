import pandas
data = pandas.read_csv("C:\python\day25\2018_Squirrel_Census.csv")
grey_squirrels = data[ data["Primary Fur Color"] == "Gray"]
print(grey_squirrels )