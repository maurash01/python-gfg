# FInd new salary on basis of :
'''
rat > 4 
 exp > 10
  hike- 20%
 exp < 10
  hike - 10% 

rat < 4 
 exp > 10
  hike- 10%
 exp < 10
    hike - 5%
'''

salary = int(input("Enter the salary"))
rat = int(input("Enter rating of person(0-5)"))
exp = int(input("Enter number of years of experience"))
new_sal=0
if rat >=4 :
    if exp >= 10:
        new_sal = salary + salary * 0.2 
    elif exp < 10:                    
        new_sal = salary + salary * 0.1
elif rat < 4 :
    if exp >= 10:
        new_sal = salary + salary * 0.2 
    elif exp < 10:                    
        new_sal = salary + salary * 0.1        
 
print(f"The New salary of Employee having {rat} rating and {exp} experinece is {new_sal}")