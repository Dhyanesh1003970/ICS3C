def pt():
  for i in range(1, 101):
      for j in range(i, 101):
        for k in range(1, 101):
           t=[]
           left = i**2 + j**2
           right = k**2
           if left == right:
              t.append(i)
              t.append(j)
              t.append(k)
              i=i**2
              j=j**2
              k=k**2
              print(t , end='')
              print('=> ', end='')
              print(i,'+',j,'=',k)
              
pt()
