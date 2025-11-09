# Find the vowel in given string 
s = 'PythonClassroomLearning'
v = 'aeiouAEIOU'
count = 0 

for i in s:
    if i in v : 
        count +=1

print(count)    