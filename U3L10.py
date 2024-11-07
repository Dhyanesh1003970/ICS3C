import math


#def p():
#    for i in range(1, 101):
      #  for j in range(i, 101):
       #     for k in range(1, 101):
        #        t=[]
         #       left = i**2 + j**2
          #      right = k**2
           #     if left == right:
            #        t.append(i)
             #       t.append(j)
              #      t.append(k)
               #     i=i**2
                #    j=j**2
                 #   k=k**2
                  #  print(t , end='')
                   # print('=> ', end='')
                    #print(i,'+',j,'=',k)
              


def pt(max):
    n=3
    max += 1
    while(n<max):
        if(n%2!=0):
            if(n>=3):
                x = pow(n,2)
                t = math.pow((n//2)*(n+1),2)
                x=x+t
                y=math.pow([n//2]*(n+1),2)
                if(x==y):
                    a = n**2
                    b = [n//2]*(n+1)
                    c = [n//2]*(n+1)+1
                    
        elif(n%2==0):
            if(n>=3):
                m=n**2/4
                a = n
                b = m-1
                c = m+1
    
    
        n+=1
    
    return[a,b,c]
                
                


pt(100)
