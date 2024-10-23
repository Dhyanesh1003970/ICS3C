import math


num = int(input('Enter the number of photos: '))

while(num <= 0):
  print('Please enter a number greater than zero')
  num = int(input('Enter the number of photos: '))

ma = math.floor(math.sqrt(num))
x = 1

print(ma, 'ma')

while(ma*x != num):
  x=x+1
  #print(x)
  if(x*ma==num):
    print(x,'x',ma)
  else:
    print('goodbye')
