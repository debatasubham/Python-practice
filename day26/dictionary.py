#dictionary comprehension
import random
names = ["subham" , "satyam" , "aman" , "tutu" , "jagan"]
students_score = {student:random.randint(1,100) for student in names}
print(students_score)


passed_students = {student:score for (student,score) in students_score.items() if score >= 60}
print(passed_students) 
# to find how many letter in each word in sentence
sentence = "what is the airspeed velocity of an unladen swallow"
result = {word:len(word) for word in sentence.split()}
print(result)