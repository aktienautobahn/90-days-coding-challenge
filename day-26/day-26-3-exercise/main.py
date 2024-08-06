import pandas as pd

with open('/Users/emilskorov/Sandbox/python/day-26/day-26-3-exercise/file1.txt') as file1:
    nums1 = file1.readlines()

with open('/Users/emilskorov/Sandbox/python/day-26/day-26-3-exercise/file2.txt') as file2:
    nums2 = file2.readlines()

result = [int(num) for num in nums1 if num in nums2]

# Write your code above 👆

print(result)


