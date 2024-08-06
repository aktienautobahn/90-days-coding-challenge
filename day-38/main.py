import os
from utils import save_to_sheety, workout_nlp, get_sheety_workouts

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 176
AGE = 37


os.system('cls' if os.name == 'nt' else 'clear')

#workout_nlp(GENDER, WEIGHT_KG, HEIGHT_CM, AGE)
save_to_sheety(workout_nlp(GENDER, WEIGHT_KG, HEIGHT_CM, AGE))
#get_sheety_workouts()