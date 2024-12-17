filename= 'wordle.dat'

fh=open(filename, 'r')



def sort(X, i, j):
    y = X[i]
    X[i] = X[j]
    X[j] = y


months=[]
years=[]
date=[]
words=[]
for i in range (1038):
    wrd = fh.readline()
    wrd.strip()
    
    mon, dat, yer, wrd=wrd.split()
    
    d = mon, dat, yer
    date.append(d)
    
    words.append(wrd)
    




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




if (wd == 'w'):
    word = input('What word are you looking for? ')
    word = word.upper()
else:
    year = input('Enter the year: ')
    year1=int(year)
    
    month = input('Enter the month (3-letter abbreviation, as in Jan for January): ')
     
    Date = input('Enter the date: ')
    Date1 = int(Date)
    
    
    
    
    


            
                
    
    month= month.replace("'", " ")
    dt = month, Date, year
    print(year1, month2, Date1)
    
d=[]
w=[]    
    

if (wd=='d'):
    for i in range(len(mths)):
        if(month==mths[i]):
            month2 = mths2[i]
    
    
    
    
    for i in range(len(date)):
        if dt==date[i]:
            print(words[i])
            w.append('1')
    


if (wd=='w'):
    for i in range(len(mths)):
        if(month==mths[i]):
            month2 = mths2[i]
        
    
    
    
    
    for i in range(len(words)):
        if(word == words[i]):
            
            mnth, day, yar = date[i].strip()
            for i in range(len(mths)):
                if(mnth==mths[i]):
                    mnth = mths2[i]
            
            print(date[i])
            d.append('1')
            


if(wd=='w'):
    if(len(d)==0):
        print('Word is not in Database')

if(wd=='d'):
    if(len(w)==0):
        print('This date is not in Database')


fh.close()
