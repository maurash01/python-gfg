# Find the sum of all the odd numbers between 1 to 100

sum = 0 
for i in range(1,101):
    if i%2 == 1 :
        sum = sum + i
print(sum)