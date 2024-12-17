filename= 'wordle.dat'

fh=open(filename, 'r')




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












def sort(X, i, j):
    y = X[i]
    X[i] = X[j]
    X[j] = y



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










for i in range(len(words)):
        for j in range(len(words)):
            if (words[i] < words[j]):
                sort(words, i, j)
                sort(date, i, j)
            
                
                
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
    print('-----------------------------------------------------------------')
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
    
    print('-----------------------------------------------------------------')
    year = input('Enter the year: ')
    year1=int(year)
    print('---------------------------------')
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
        print('Word is not in Database')

if(wd=='d'):
    if(len(w)==0):
        print('This date is not in Database')


fh.close()

