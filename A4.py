filename= 'wordle.dat'

fh=open(filename, 'r')



def merge(arr, l, m, r, date):
    n1 = m - l + 1
    n2 = r - m
    
    L = [0] * (n1)
    R = [0] * (n2)
    L2 = [0] * (n1)
    R2 = [0] * (n2)
    
    for i in range(0, n1):
        L[i] = arr[l + i]
        L2[i] = date[l+i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
        R2[j] = date[m+1+j]
    
    i = 0  
    j = 0  
    k = l  
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            date[k] = L2[i]
            i += 1
        else:
            arr[k] = R[j]
            date[k]= R2[j]
            j += 1
        k += 1
    
 
    while i < n1:
        arr[k] = L[i]
        date[k] = L2[i]
        i += 1
        k += 1
    
   
    while j < n2:
        arr[k] = R[j]
        date[k]=R2[j]
        j += 1
        k += 1







def mergesort(arr, l , r, date):
    
    if (l<r):
        m = l + (r-l)//2
        mergesort(arr , l , m, date)
        mergesort(arr, m+1, r, date)
        merge(arr, l , m , r, date)











def merge1(p,q,r):
    mths=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    mths2=['01','02','03','03','05','06','07','08','09','10','11','12']
    
    if(wd=='w'):
        for j in range(len(mths)):
                if(x==mths[j]):
                    mnth = mths2[j]
                    print(' is the solution on', r, mnth, q)



    else:
        for i in range(len(mths)):
            if(p==mths[i]):
                month2 = mths2[i]
                print('On', r,month2,q, end='' )
                return













date=[]
words=[]
for i in range (1038):
    wrd = fh.readline()
    wrd.strip()
    
    mon, dat, yer, wrd=wrd.split()
    
    d = mon, dat, yer
    date.append(d)
    
    words.append(wrd)

l = len(words)


mergesort(words, 0, l-1, date)




            
                
                
print('Welcome to the Wordle Database')
wd = input('Enter w if you are looking for a word, or d for a word a certain date: ')

if wd == wd.upper():
    wd = wd.lower()
    
mths=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mths2=['01','02','03','03','05','06','07','08','09','10','11','12']



d=[]
w=[]


if (wd == 'w'):
    m=[]
    print('------------------------------------------------------------------------')
    word = input('What word are you looking for? ')
    word = word.upper()

        
    
    
    
    
    for i in range(len(words)):
        if(word == words[i]):
            a = date[i]
            m.append(a)

            x = a[0]
            mnth=2
            
            for j in range(len(mths)):
                if(x==mths[j]):
                    mnth = mths2[j]
            
            
         
            print()
            print('The word',word, end='')
            merge1(mnth, a[1], a[2])
            
            d.append('1')
            
            
            
            
            
            
            
else:
    
    print('------------------------------------------------------------------------')
    year = input('Enter the year: ')
    year1=int(year)
    print('--------------------')
    month = input('Enter the month (3-letter abbreviation, as in Jan for January): ')
    print('---------------------------------')
    Date = input('Enter the date: ')
    Date1 = int(Date)
    
    
    dt = month, Date, year
   
    
    
    

    print()
    merge1(month, Date, year)
    
    
    
    
    for i in range(len(date)):
        if dt==date[i]:
            print(' the soltion was', words[i])
            w.append('1')
    



    
            


if(wd=='w'):
    if(len(d)==0):
        print()
        print('Word is not in Database, please check agian')

if(wd=='d'):
    if(len(w)==0):
        print()
        print('This date is not in Database', end='')
        print(', please check the date and rerun program,(check the capital letter on month)')


fh.close()

