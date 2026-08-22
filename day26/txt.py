with open("txt_file.txt") as file1:
    file_1_data = file1.readlines()

with open("txt_2file.txt") as file2:
    file_2_data = file2.readlines() 

result = [int(num)for num in file_1_data if int(num) in file_2_data]

print(result)
