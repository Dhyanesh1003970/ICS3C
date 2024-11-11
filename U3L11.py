import random

def shuff(s):
  t=[]
  s +=1

  x = random.randrange(1,s)
  t.append(x)
    
  for i in range (1,s):
      
    x= random.randrange(1,s)

    t.append(x)
         

       
        
  print(t)
    
    

shuff(6)
