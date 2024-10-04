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
