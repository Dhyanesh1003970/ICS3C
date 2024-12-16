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
    
    words.append(wrd)
    months.append(mon)
    date.append(dat)
    years.append(yer)
    
   



for i in range(len(words)):
        for j in range(len(words)):
            if (words[i] < words[j]):
                sort(words, i, j)
                sort(date, i, j)
                sort(months, i, j)
                sort(years, i, j)
                
                
print('Welcome to the Wordle Database')
wd = input('Enter w if you are looking for a word, or d for a word a certain date: ')

if wd == wd.upper():
    wd = wd.lower()
    

mths = [Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec]


if (wd == 'w'):
    word = input('What word are you looking for? ')
    word = word.upper()
    print(word)
else:
    month=()
    year = input('Enter the year: ')
    year=int(year)
    month = input('Enter the month (3-letter abbreviation, as in Jan for January): ')
    Date = input('Enter the date: ')
    Date = int(Date)
    
    
    for i in range(len(mths)):
        if month == mths:
            month=mths[i]
    
    
    dt = month, Date, year
    print(dt)
    
    
    
    
    
    
    
    
    
    
    
    
    

if (wd=='d'):
    
    for i in range(len(date)):
        if dt==date[i]:
            print(word[i])

if (wd=='w'):
    for i in range(len(words)):
        if(word == words[i]):
            print(date[i])



fh.close()
