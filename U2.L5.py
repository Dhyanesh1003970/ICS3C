totel = 1
total = 0
num=float(input("Give a number: "))
print('Counting from j = 1 to',num,':')
print(' j   tri       factorial')
count = 0
while(count < num ):
  count+= 1
  print('%4d' % count, end = '')
  total = total + count
  print('%7d' % total, end='')
  totel = totel * count
  print('%10d' % totel)
