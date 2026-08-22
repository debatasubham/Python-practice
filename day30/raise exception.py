height = float(input("Enter your height in meters: "))
if height >3:
    raise ValueError("Human height should not be over 3 meters.")
weight = int(input("enter your weight in kg : "))
bmi = weight / height**2
print(bmi)
