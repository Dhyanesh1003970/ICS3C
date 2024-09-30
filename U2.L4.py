total = 1
n = int(input('Enter a whole # > 0: '))
count = 0
while(count < n):
  count += 1
  print(count)
  total = total * count
print('triangular number', n, '=', total)
