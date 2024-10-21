ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
      
  print()

ar1 = [3,4,1,2,6]
ar22= [9,2,3,7,5]
ar33= [4,2,1,0,3]
total = 0
t = []
for i in range(len(ar1)):
  total = total + ar1[i]
  
t.append(total)
total = 0
for i in range(len(ar22)):
  total = total + ar22[i]
  
t.append(total)
total = 0

for i in range(len(ar33)):
  total = total + ar33[i]
  
t.append(total)

print(t)
