import random

a = [1, 2, 3, 4, 5, 6]


def shuff(s):
  
  t=[]
  g=1
  for i in range (0,s):
    x = random.randrange(1,s)
    j = a[x]
    t.append(j)
       
        
  print(t)
    
    

shuff(6)
