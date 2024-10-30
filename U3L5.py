#modification 1


a = (input('Enter a number:'))
b = (input('Enter another number: '))

try:
  a =int(a)
  b =int(b)

except:
  a = float(a)
  b = float(b)

def add(a, b):
  return a + b


print(add(a, b)*2)


#modification 2

m =int(input('Enter a number: '))
n =int(input('Enter a number: '))

def myPow():
  return m**n
  
  
print(myPow())
