'''

first_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))

print("Hi",first_name," your age is ",user_age,".")

'''

# Program 2 
'''
name = input("Enter your name : ")
grade = input("Enter your grade : ")
marks = int(input("Enter your marks: "))

#print("Hi",name,"your grade is",grade,"and your marks are",marks)

print(f"Hi {name},your grade is {grade},and your marks are {marks}")

'''

# Program 3 
# Find simple interest i.e. (P*R*T)/100

principal = int(input("Enter principal amount: "))
rate = int(input("Enter rate : "))
time = int(input("Enter Time : "))   
SI = (principal * rate * time)/100
print (SI)


