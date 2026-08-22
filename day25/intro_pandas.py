import pandas 
data = pandas.read_csv(r"C:\python\day25\weather_data.csv")
print(f"The type of data is {type(data)}")
print(data)
data_dict = data.to_dict()
print(data_dict)

temp_list =data["temp"].to_list()
print(temp_list)
average = sum(temp_list)/len(temp_list)
print(f"average temperature is {average}")
print(data["temp"].mean())


print(data["temp"].max())   
print(data["condition"])    
print(data["day"])
print(data.condition)

#get data in row
print(data[data.day == "monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day=="monday"]
monday_temp = int(monday.temp.iloc[0])
monday_temp_f = monday_temp * 9/5 + 32  
print(f"monday temp is {monday_temp_f}")     

data_dict = {
    "stydents":["subham","satyam","tutu","aman"],
    "scores":[85,88,80,92]
}

dataframe = pandas.DataFrame(data_dict)
print(dataframe)
dataframe.to_csv("student_data.csv")
