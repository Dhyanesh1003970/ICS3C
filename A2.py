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
    

    t=[]
    
    while(x<=num):
        if (num%x==0):
            if(x != num):
                if(x != 1):
                    if(num / m != m):
                        print(x)
                    elif(num / m == m):
                        t.append(x)
                        
                         
        x = x+1


    if(len(t)==1):
        print(t)
    num = (input('Enter the number of photos: '))
