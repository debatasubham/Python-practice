numbers=[1,2,3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

name = "subham"
new_name = [letter for letter in name]
print(new_name)

range_list = [num*2 for num in range(1,5)]
print(range_list) 

names = ["subham" , "satyam" , "aman" , "tutu" , "jagan"]

new_names = [name.upper() for name in names if len(name) > 5]
print(new_names)

nos = [1,1,2,3,5,8,13,21,34,55]
new_nos = [n*n for n in nos]
print(new_nos)
even_nos = [n for n in nos if n % 2 == 0]
print(even_nos)
