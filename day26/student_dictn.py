student_dict = {
    "student":["subham" , "satyam" , "tutu"],
    "score" : [89 , 56 , 78]

}
    
#  looping through dictionaries
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# loop through rows of a data frame
for (index,row) in student_data_frame.iterrows():
   # print(row.student)
    if row.student == "satyam":
        print(f"the score of {row.student} is {row.score}")
