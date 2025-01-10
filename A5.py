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
        L[i] = arr[l + i]
        #temp arrays
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
            gn[k] = L2[i]
            sn[k] = L3[i]
            cct[k] = L4[i]
            ccn[k] = L5[i]
            emo[k] = L6[i]
            eyr[k] = L7[i]
            
            
            
            #sorting list
            i += 1
        else:
            arr[k] = R[j]#sorting list
            gn[k]= R2[j]#sorting list
            sn[k] = R3[j]
            cct[k] = R4[j]
            ccn[k] = R5[j]
            emo[k] = R6[j]
            eyr[k] = R7[j]
            
            j += 1
        k += 1
    
 
    while i < n1:
        arr[k] = L[i]#sorting list
        gn[k] = L2[i]#sorting list
        sn[k] = L3[i]
        cct[k] = L4[i]
        ccn[k] = L5[i]
        emo[k] = L6[i]
        eyr[k] = L7[i]
        i += 1
        k += 1
    
   
    while j < n2:
        arr[k] = R[j]#sorting list
        gn[k] = R2[j]#sorting list
        sn[k] = R3[j]
        cct[k] = R4[j]
        ccn[k] = R5[j]
        emo[k] = R6[j]
        eyr[k] = R7[j]
        j += 1
        k += 1
        






def mergesort(arr, l , r, gn, sn, cct, ccn, emo, eyr): #merge sort function part 1
    
    if (l<r):
        m = l + (r-l)//2#splitting array to smaller bits
        mergesort(arr , l , m, gn, sn, cct, ccn, emo, eyr)# recursion
        mergesort(arr, m+1, r, gn, sn, cct, ccn, emo, eyr)#recrusion
        merge(arr, l , m , r, gn, sn, cct, ccn, emo, eyr)#calling sorting function





def merge1(m, y ): # merge function for turning months to integers 
   

       
    m = int(m)   
    y = int(y)
    y = y * 100 
    
    full = y + m
    
    return (full)
    









filename = 'data.dat'

fh = open(filename, 'r')


title = fh.readline()




gn = []
sn = []
cct = []
ccn = []
emo = []
eyr = []
fulldate=[]




for i in range (200):
    l = fh.readline()
    
    #for j in range (len(l)):
     #   if l[j]==',':
      #      l[j]=' ' 
    
  
    
    l.strip()
    g,s,c,cn,m,y = l.split(',')
    gn.append(g)
    sn.append(s)
    cct.append(c)
    ccn.append(cn)
    emo.append(m)
    eyr.append(y)
    
    


for i in range (len(eyr)):
    date = merge1(emo[i], eyr[i])

    date = str(date)
    
    fulldate.append(date)



len = len(fulldate)



mergesort(fulldate, 0, len-1, gn, sn, cct, ccn, emo, eyr)


fh.close



for i in range(200):
    full = int(fulldate[i])

    if(full < 202501):
        print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i], ' expired')
    
    elif(full == 202501):
        print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i], 'RENEW NOW')
        
    elif(full > 202501):
        print(gn[i],sn[i],cct[i],ccn[i],emo[i],eyr[i], 'safe')
    
    
