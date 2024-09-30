import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
while(y<=0):
  print('Please do not enter 0, zero divison is not possible')
  y = input('Please input nonzero whole numnber')
  y =int(y)
rem = x % y
if rem == 0:
    print('Yes', y, 'is a facotr of',x)
else:
  print("Now deciding if", y, "is a factor of", x, "...")
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
  else:
    print(y, 'is not a facotor of', x)
  
