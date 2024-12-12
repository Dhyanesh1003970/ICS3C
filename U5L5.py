ar=[]

x = 0
y = 1

ar.append(x)
ar.append(y)

temp = input('Enter a number: ')
temp = int(temp)-1

print(x)
print(y)

for j in range(temp):
    r = len(ar)-2
    q = len(ar)-1

    x2 =ar[r]
    y2=ar[q]

    t = x2 + y2
    print(t)
    ar.append(t)
