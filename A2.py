''' 
Name: Dhyanesh Murugesan
Course: ICS3C0-2


Variable dictionary:
num = user input(int)
d = varible for end program(string)
x = starting loop(int)
m = square root of num and rounded down(int)
t = answer of perimeter(int)
'''



print('Hello, welcome to photo organzier, answer the question to recieve the deminsions, Enter the word done when you are done with the program')

print()

import math #math libaray
d = 'done' #Varible for end program

num = (input('Enter the number of photos: ')) #user input, variable defined as 'num'

while(num != d): #Will continue to loop until the user input equals 'd'
  
    x=1 

    num = int(num)
    while(num <= 0): # will continue to loop if user keeps inputing the number<=0
        print('Please enter a number greater than zero')
        print()
        num = int(input('Enter the number of photos: '))
        num = int(num)#Data change
    m = math.floor((math.sqrt(num))) #Takes input of user and finds the square root than rounds down


  
    while(x<=num): #Factoring part of the codes
      
        if(num%m!=0): #Seeing if input is a factor of 'm'
            m=m+1 #If not, 1 in added to 'm'
        
        if (m*x==num):
            print(m ,'x', x)#deminsions
            t = 2*(m+x) #formula for perimeter
            print('The minimum perimeter would be:', t)
            
            
        x = x+1
    
    print()             
    num = (input('Enter the number of photos: '))#loop
