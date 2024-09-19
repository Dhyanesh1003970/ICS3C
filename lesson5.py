import math 
print('#1')
lenght = input('Please enter one of the sides of the square: ')
lenght = float(lenght)
area = math.pow(lenght,2)
print(' ')
print('The area of the square is:', area)

print('  ')
print('  ')


print('#2')
print('AREA OF A NORMAN WINDOW')
print('  ')
lenght = input('Please enter measurement of one side of the square')
lenght = float(lenght)
area1 = math.pow(lenght, 2)
area1 = float(area1)
print('  ')
print('Area of squaqre:', area1)
print('  ')
radius = input('Please type radius of semi-circle: ')
area2 = math.pow(math.pi, 2)
area2 = float(area2)
area2 = area2 * 0.5
area2 = float(area2)
print('  ')
print(area2)
total =  area1 + area2
print('  ')
print('total area', total)
