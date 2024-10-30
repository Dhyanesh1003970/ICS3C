

n = int(input('Enter a number: '))

while(n >= 0):
    t = []



    def factorize():
        j=1
        while(j<=n):
            if(n%j==0):
                if(j != n):
                    t.append(j)
            j += 1


    factorize()


    total = 0
    for i in range(len(t)):
        total = total + t[i]
  
    print('The sum of the factors is :', total)

    if(total<n):
        print(n,'is a deficient')

    elif(total==n):
        print(n, 'is a perfect number')
    
    elif(total>n):
        print(n,'is a abundant number')
        
        
    print()
    n = int(input('Enter a number: '))
    
    
print('good bye')
