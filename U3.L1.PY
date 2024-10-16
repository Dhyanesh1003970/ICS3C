x = input('Enter your grade: ')
x = int(x)
if(80 <= x <= 100):
  print('You have an A, Good job')
elif(70 <= x <= 79):
  print('You have a B, Nice')
elif(60 <= x <= 69):
  print('You have a C, Getting close to success')
elif(50 <= x <=59):
  print('You have a D, Determination Gets Success')
elif(x < 50):
  print('You have an F, Keep Trying')
