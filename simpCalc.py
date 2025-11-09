# Make a simple Calculator 
num=0
num1 = float(input("Enter number 1 : "))
num2 = float(input("ENter number 2 :"))

op = input(" Choose opertor b/w (+,-,*,/)  : ")

if op == '+' :
    num = num1+num2 
elif op == '-':
    num = num1-num2 
elif op == '*' :
    num = num1*num2 
elif op == '/':
    if num2 == 0:
        print("Cannot be divided by zero")
    else:
        num = num1/num2 
else:
    ("Invalid Operator")
print(num)                    