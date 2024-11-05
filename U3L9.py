L = input("how many lines are you inputing? ")

L =int(L)




c = 'C'
g = 'G'
t = 'T'
a = 'A'

for j in range (L):
  p=[]

  def comp(dna):
    
    c = 'C'
    g = 'G'
    t = 'T'
    a = 'A'
 
    for i in range (len(dna)):
      if(dna[i]==c):
        G='G'
        p.append(G)
     
      elif(dna[i]==g):
        C='C'
        p.append(C)
     
      elif(dna[i]==t):
        A='A'
        p.append(A)
     
      elif(dna[i]==a):
        T='T'
        p.append(T)

       
    print(p)
    
 
 
  def validate():
      if(len(p)== len(dna)):
        print('Valid')
        
       
      else:
        print('Not valid:', end='')
        for i in range(len(dna)):
            if(dna[i]==c):
              x=1
    
            elif(dna[i]==g):
              x=1
    
            elif(dna[i]==t):
              x=1
     
            elif(dna[i]==a):
              x=1
          
            else:
              j = i+1
              print(dna[i],'found in position', j )
  


  
  
  
  print()     
  dna = input('Input strand: ')

  comp(dna) 
  validate()
