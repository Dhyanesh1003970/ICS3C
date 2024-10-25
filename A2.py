import math
d = 'done'

num = (input('Enter the number of photos: '))

while(num != d):
  
    x=1

    num = int(num)
    while(num <= 0):
        print('Please enter a number greater than zero')
        num = int(input('Enter the number of photos: '))
        num = int(num)
    m = math.floor((math.sqrt(num)))
    
   # print(m)
    
    
    
    while(x<=num):
        if(num%m!=0):
            m=m+1
        
        if (m*x==num):
            print(m ,'x', x)
            t = 2*(m+x)
            print('The minimum perimeter would be:', t)
            
            
        x = x+1
    
                        
    num = (input('Enter the number of photos: '))
