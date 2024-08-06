import os

cwd = os.getcwd()  
# for f in os.listdir(cwd):
# 	print(f)

print(cwd)      

# with open(cwd + '/data.txt') as data:
#  	high_score = int(data.read())
 
with open('data.txt') as data:
	high_score = int(data.read())
print(high_score)