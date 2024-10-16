import math
print('  N|  SQR|  Cubes|Roots')
print('---+-----+-------+-----')


s = 1
for i in range(10,200,15):
  print("%3d|" % i, end='')
  print('%5d|' % i**2, end ='')
  print('%7d|' % i**3, end ='')
  print('%5.2f' % math.sqrt(i) )
