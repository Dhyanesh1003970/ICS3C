def validate(N):
    total1=0
    total=0
    temp = []
    temps1=[]
  
  
    for i in range(len(num)):
        if i%2 != 0:
            temp.append(t[i])  
        
    for i in range(len(temp)):
        temp1 = int(temp[i])
        temps = temp1+temp1
        temps1.append(temps)
  
    
    for i in range(len(temps1)):
        total = total + temps1[i]
    
    for j in range(len(t)):
        if j%2==0:
            tj = int(t[j])
            
            total1 = total1 + tj
    
    
    total = total + total1
    
    
    return total

  
print("Validate a number with the Luhn Algorithm!")
num = input("Input a number to validate: ")

num = num.strip()

t=[]


for i in range(len(num)):
  t.append(num[i])



isValid = validate(num)
if isValid%10==0:
    print(num, "is valid!")
else:
    print(num, "is not valid!")
