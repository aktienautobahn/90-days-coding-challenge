'''
first dict comprehensions trial
'''
from random import randint
names = ['Andrew', 'Alex', 'Berth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_scores = {}

student_scores = {name:randint(0,100) for name in names}
passed_students = {name:value for (name,value) in student_scores.items() if value > 59}
print(student_scores)
print(passed_students)
