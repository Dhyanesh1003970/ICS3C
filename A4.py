'''
Name: Dhyanesh Murugesan
Student number: 1003970
Due date: December 20, 2024
Course: ICS3U0-2



VARIABLE DICTIONARY:

Driver code:

filename - wordle file 

fh - command for opening, reading and closing file 

date - array to store the dates read in the file 

words - array to store the words read in the file 

wrd - line of each line read

D - One variable for the date(month date and year)

l - length of the array words

wd - user input to search for word or date 

mths - array with all the months order with the first three letter 

mths2 - array with the numbers repect full to the month

d - corrections array if the user is searching for a date with a certain word

w - corrections array if the user is searching for a word on a certain date

word - asks for input if the user is searching for the date of the word 

a - date relative to the word searched 

x - taking the month of the date 

mnth - the number of the month

year - asking user for the year if the user is searching for a certain word on a certain date

year1 - duplicate of year 

month - asking user for the month

Date - asking user for the date

Date1 - duplicate of Date 

dt - the dates asked put into one variable (month, date, year)

functions:
    mergesort:
    
        m - variable to split up the array for merge sort 

    merge:
        n1 -
        
        n2 -
        
        L - temp array 
        
        R - temp array 
        
        L2 - temp array
        
        R2 - temp array 
        
        arr - replacer array
       


'''













filename= 'wordle.dat' # opening file

fh=open(filename, 'r')#defining file read



def merge(arr, l, m, r, date):#merge sort function part 2
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







def mergesort(arr, l , r, date):#merge sort function part 1
    
    if (l<r):
        m = l + (r-l)//2
        mergesort(arr , l , m, date)
        mergesort(arr, m+1, r, date)
        merge(arr, l , m , r, date)











def merge1(p,q,r): # merge function for turning months to integers 
    mths=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #these arrays class the months to their respected number 
    mths2=['01','02','03','04','05','06','07','08','09','10','11','12']
    
    if(wd=='w'):
        for j in range(len(mths)):
                if(x==mths[j]):
                    mnth = mths2[j]
                    print(' is the solution on', r, mnth, q)
                    return



    else:
        for i in range(len(mths)):
            if(p==mths[i]):
                month2 = mths2[i]
                print('On', r,month2,q, end='' )
                return













date=[]#array for dates
words=[]#array for words
for i in range (1038):#loop for reading lines
    wrd = fh.readline()#reading lines 
    wrd.strip()#part 1 of spilting the word from the date
    
    mon, dat, yer, wrd=wrd.split()#date and word sperated
    
    D = mon, dat, yer#month date and year sorted in one variable
    date.append(D)#puts it into the apporpirate array
    #along with the word
    words.append(wrd)

l = len(words)#counting how many words are in the array


mergesort(words, 0, l-1, date)#callin merge function part 1



fh.close()
            
                
                
print('Welcome to the Wordle Database') #introduciton
wd = input('Enter w if you are looking for a word, or d for a word a certain date, enter done once you are done: ')
#input for what the user is looking for


if (wd!='w' or'd'):
    print('Please input w or d only')
    wd = 'done'


while (wd != 'done'):#loop

    if wd == wd.upper():
        #if the user inputs an uppercase letter, it will lowercase for better interpretation
        wd = wd.lower()
    
    mths=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    #these arrays class the months to their respected number 
    mths2=['01','02','03','03','04','05','06','07','08','09','10','11','12']



    d=[]
    #correction arrays
    w=[]


    if (wd == 'w'): #checking if it is a word search or date search
    
        print('------------------------------------------------------------------------')# spacer
    
        word = input('What word are you looking for? ')#word input
        word = word.upper()#upWelcome to the Wordle Database

    
    
    
    
        for i in range(len(words)):
            #searching for the word inputted in the data file
            if(word == words[i]):
                #once found, it is put into an array
                a = date[i]
            

                x = a[0]#taking the month in the array
            
            
                for j in range(len(mths)):
                    #searching for the month an another array
                    if(x==mths[j]):
                        #once found it is put into a variable
                        mnth = mths2[j]
            
            
         
                print()
                print('The word',word, end='')
                merge1(mnth, a[1], a[2])#calling function that classes each month to its repected number 
            
                d.append('1')#correction array
            
            
       
            
            
            
            
    else:
    
        print('------------------------------------------------------------------------')#spacer
        year = input('Enter the year: ')#user asked to input year 
        year1=int(year)#temp array
        print('--------------------')#spacer
        month = input('Enter the month (3-letter abbreviation, as in Jan for January): ')#user asked to input month
        print('---------------------------------')#spacer
        Date = input('Enter the date: ')#user asked to input date
        Date1 = int(Date)#temp array
    
    
        dt = month, Date, year # all classes into one array
   
    
    
    

        print()
        merge1(month, Date, year)#calling function that classes each month to its repected number 
    
    
    
    
        for i in range(len(date)):
            #searching for date in another array 
            if dt==date[i]:
                print(' the soltion was', words[i])
                w.append('1')#correction array
    



    
            


    if(wd=='w'):
        #checking if it has the right number of list, so it knows it is right
        if(len(d)==0):
            print()#spacer
            print('Word is not in Database, please check agian')

    if(wd=='d'):
         #checking if it has the right number of list, so it knows it is right
        if(len(w)==0):
            print()
            print('This date is not in Database', end='')
            print(', please check the date and rerun program', end='')
            print('check the capital letter on month,' end='')
            print('and in data base, words start at 2021 06 19 and end at 2024 04 21)')#error message
            #error message

    print()#spacer
    wd = input('Enter w if you are looking for a word, or d for a word a certain date, enter done once you are done: ')#loop


print('Goodbye')
