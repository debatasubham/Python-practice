# to convert Celcius to fahrenheit
# formula = (Temperature in Celsius * 9/5)+32

weather_c = {"monday":12 , "tuesday":14 , "wednesday":15 , "thursday":14 , "friday":21 ,"saturday":22 , "sunday":24}

weather_f = {day:(temp*9/5)+32 for (day,temp) in weather_c.items()}
print(weather_f)
