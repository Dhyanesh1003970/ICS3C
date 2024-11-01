L = input("how many lines are yiou inputing? ")

L =int(L)

for j in range (L):

  def comp(dna):

    c = 'C'
    g = 'G'
    t = 'T'
    a = 'A'
 
    for i in range (len(dna)):
      if(dna[i]==c):
        print('G', end='')
      
      elif(dna[i]==g):
        print('C',end='')
      
      elif(dna[i]==t):
        print('A', end='')
      
      elif(dna[i]==a):
        print('T', end ='')
  
    
       
  dna = input('Input strand: ')


  print('Complementary string : ', end='')
  x=comp(dna)
  
  print()
  
  if(len(x)==len(dna)):
