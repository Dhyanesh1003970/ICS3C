#modification 1
s = '#'
for i in range(10,0,-1):
  print(s*i)
  
#modification 2
rows = int(input("Enter number of rows: "))

k = 0

for i in range(1, rows+1):
    for space in range(1,(rows-i)+1):
        print(end="  ")
   
    while k!=(2*i-1):
        print("# ", end='')
        k += 1
    k = 0
    print()

#modification 3
n=input('Input the number of rows: ')
n=int(n)
s = '#'
for i in range (n):
   for j in range(n-i-1):
       print(' ',end='')
   for j in range(2*i+1):
       print('#', end='')
   print()


for i in range(n):
   for j in range(i):
       print(' ',end='')
   for j in range(2*(n-i)-1):
       print("#",end="")
   print()


