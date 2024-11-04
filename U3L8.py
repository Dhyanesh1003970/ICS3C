L = input("how many lines are yiou inputing? ")

L =int(L)

p = []

for j in range (L):


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
       
      else:
        print('error')
       
    print(p)
    
 
 
  def validate():
    for i in range(len(p)):
      if(p[i] != 'A', 'C', 'G', 'T'):
        print('Valid')
       
      else:
        print('error')
  
  
  
  
  
  print()     
  dna = input('Input strand: ')

comp(dna) 
