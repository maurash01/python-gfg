'''
age = 18
if age >= 18:
    print("Eligible")
else:
    print("Not Eligible")    
'''

# find the number is even or odd 
'''
num = int(input ("Enter a number:"))

if num % 2 == 0:
    print("The number is EVEN")
    
else:
    print("The Number is Odd")    
    
'''

# Give grade : 100-90 : A, 90-80 : B, 80-70 : C, 70-60 : D, else FAIL 

num = int(input("Enter a number:")) 
if num <= 100 and num > 90:
    print ("A") 
elif num <=90 and num > 80 :
    print("B")
elif num <=80 and num > 70:
    print("C")
elif num <= 70 and num > 60:
    print("D")
else :
    print("Fail")        
                