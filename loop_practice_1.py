# Find the sum and count of first 7 numbers which are divisble by 7 and 11 in range of 1 to 10000

sum = 0 
count = 0 

for i in range(1,10001):
    if i % 7 == 0 and i % 11 == 0  :
        sum = sum + i 
        count +=1     
    if count == 7:
        break 
print(f"The count is {count} and the sum is {sum}") 
    