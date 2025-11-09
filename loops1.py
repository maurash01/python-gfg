# ENter table in reverse
'''
num = int(input("Enter a number : "))
for num in range((num*num),num-1,-num):
    print(num)
    
'''

# Enter table in full format 

num = int(input("Enter a number : ")) 
for i in range(1,11):
    print(f"{num} X {i} = {num*i}") 