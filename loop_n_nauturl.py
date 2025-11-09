# Find the sum of n natural numbers 

n = int(input("Enter a number upto n "))
sum = 0 
for i in range(1,n+1):
    sum = sum+i 
print(sum)