'''
Name: Dhyanesh Murugesan
Student number: 1003970
Due date: January 23, 2025
Course: ICS3U0-2


VARIABLE DICTIONARY:

DRIVER CODE:

filename - name of the database

fh - function to read and close file

title - header of the file

gn - givenname array

sn - surname array

cct - card type array

ccn - card number array

emo - expiring month array 

eyr - expiring year array

fulldate - array for storing the combined date (202501)

l = line reading 

date = variable for merging the month and year together

len = length of fulldate array for merge sort

full = variable that turns the date into integer 

FUNCTIONS:

MERGESORT:
    m - variable to split up the array for merge sort  
    
MERGE:

    L to L7 - temp array
    
    R to R7 - temp array

    arr - replacer array
       
       
merge1:
m - Integer version of months

y - integer version of years

ful - adds the two numbers together(after y was multiplied by 100)



'''
def merge(arr, l, m, r, gn, sn, cct, ccn, emo, eyr):#merge sort function part 2
    n1 = m - l + 1
    n2 = r - m
    
    #temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    L3 = [0] * (n1)
    R3 = [0] * (n2)
    L4 = [0] * (n1)
    R4 = [0] * (n2)
    L5 = [0] * (n1)
    R5 = [0] * (n2)
    L6 = [0] * (n1)
    R6 = [0] * (n2)
    L7 = [0] * (n1)
    R7 = [0] * (n2)
    
    for i in range(0, n1):
        #temp array
        L[i] = arr[l + i]

        L2[i] = gn[l+i]
        
        L3[i] = sn[l+i]
        
        L4[i] = cct[l+i]
        
        L5[i] = ccn[l+i]
        
        L6[i] = emo[l+i]
        
        L7[i] = eyr[l+i]
        
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        #temp arrays
        R2[j] = gn[m+1+j]
        
        R3[j] = sn[m+1+j]
        
        R4[j] = cct[m+1+j]
        
        R5[j] = ccn[m+1+j]
        
        R6[j] = emo[m+1+j]
        
        R7[j] = eyr[m+1+j]
    
    i = 0  
    j = 0  
    k = l  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]#sorting list
            gn[k] = L2[i]#sorting list
            sn[k] = L3[i]#sorting list
            cct[k] = L4[i]#sorting list
            ccn[k] = L5[i]#sorting list
            emo[k] = L6[i]#sorting list
            eyr[k] = L7[i]#sorting list
            
            
            
            #sorting list
            i += 1
        else:
            arr[k] = R[j]#sorting list
            gn[k]= R2[j]#sorting list
            sn[k] = R3[j]#sorting list
            cct[k] = R4[j]#sorting list
            ccn[k] = R5[j]#sorting list
            emo[k] = R6[j]#sorting list
            eyr[k] = R7[j]#sorting list
            
            j += 1
        k += 1
    
 
    while i < n1:
        arr[k] = L[i]#sorting list
        gn[k] = L2[i]#sorting list
        sn[k] = L3[i]#sorting list
        cct[k] = L4[i]#sorting list
        ccn[k] = L5[i]#sorting list
        emo[k] = L6[i]#sorting list
        eyr[k] = L7[i]#sorting list
        i += 1
        k += 1
    
   
    while j < n2:
        arr[k] = R[j]#sorting list
        gn[k] = R2[j]#sorting list
        sn[k] = R3[j]#sorting list
        cct[k] = R4[j]#sorting list
        ccn[k] = R5[j]#sorting list
        emo[k] = R6[j]#sorting list
        eyr[k] = R7[j]#sorting list
        j += 1
        k += 1
        






def mergesort(arr, l , r, gn, sn, cct, ccn, emo, eyr): #merge sort function part 1
    
    if (l<r):
        m = l + (r-l)//2#splitting array to smaller bits
        mergesort(arr , l , m, gn, sn, cct, ccn, emo, eyr)# recursion
        mergesort(arr, m+1, r, gn, sn, cct, ccn, emo, eyr)#recrusion
        merge(arr, l , m , r, gn, sn, cct, ccn, emo, eyr)#calling sorting function





def merge1(m, y ): # merge function for putting together the year and month (202501)
   

       
    m = int(m) #data change  
    y = int(y)#data change
    y = y * 100 #times it by a 100 so we can add m
    
    ful = y + m #add them together
    
    return (ful)#returning 
    









filename = 'data.dat' # filename 

fh = open(filename, 'r')# for opening, reading and closeing


title = fh.readline()#reads the tite line




gn = [] #givenname
sn = [] # surname
cct = [] # card type
ccn = [] # card number
emo = [] #expiring month
eyr = [] # expiring year
fulldate=[] #full date both year and month(202501)




for i in range (200): # reading line
    l = fh.readline() #line reading
    
    
  
    
    l.strip()#spliting line
    g,s,c,cn,m,y = l.split(',') # spliting the line by ','
    #sending informations to the respected array
    gn.append(g) 
    sn.append(s)
    cct.append(c)
    ccn.append(cn)
    emo.append(m)
    eyr.append(y)
    
    


for i in range (len(eyr)): #loop for combineing month and year
    date = merge1(emo[i], eyr[i]) # function that will combine the month and year

    date = str(date) #data change
    
    fulldate.append(date) # date is put into array



len = len(fulldate) #length of full date array for the merge sort function



mergesort(fulldate, 0, len-1, gn, sn, cct, ccn, emo, eyr)# mergesorting function


fh.close # file close



for i in range(200):# checking the cards
    full = int(fulldate[i])#data change

    if(full < 202501):#checking if it is expired
        print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i] , end=' ')#if so it will print the card informatation
        #and print EXPIRED
        print('EXPIRED')
        print()
    elif(full == 202501):#checking if it is about expired
        print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i] , end=' ')#if so it will print the card informatation
         #and print EXPIRED
        print('RENEW IMMEDIATELY')
        print()
    
    #elif(full > 202501):
     #   print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i],end='' 'SAFE')
    
    
