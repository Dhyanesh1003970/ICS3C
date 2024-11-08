import math

def pt(max):
    n=3
    max=int(max)
    max += 1
    while(n<max):
            t=[]
            if(n%2!=0):
                if(n>=3):
                   x = n**2+(n//2*n+1)**2
                   y=((n//2*n+1)+1)**2
            
                if(x==y):
                    a = n
                    b = (n//2)*(n+1)
                    c = (n//2)*(n+1)+1
                    if(c<max):
                        t.append(a)
                        t.append(b)
                        t.append(c)
                        a=a**2
                        b=b**2
                        c=c**2
                        print(t , end='')
                        print('=> ', end='')
                        print(a,'+',b,'=',c)
                        
            if(n%2==0):
                if(n>=3):
                    m=n**2//4
                    a = n
                    b = m-1
                    c = m+1
                    if(c<max):
                        t.append(a)
                        t.append(b)
                        t.append(c)
                        a=a**2
                        b=b**2
                        c=c**2
                        print(t , end='')
                        print('=> ', end='')
                        print(a,'+',b,'=',c)
            
            
            n = n+1
    
    
                
                


pt(100)
