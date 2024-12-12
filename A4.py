filename= 'wordle.dat'

fh=open(filename, 'r')



def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp







date=[]
words=[]
for i in range (1038):
    wrd = fh.readline()
    wrd.strip()
    
    mon, dat, yer, word=wrd.split()
    words.append(word)
    dates = mon , dat, yer
    date.append(dates)



for i in range(len(words)):
        for j in range(len(words)):
            if (words[i] < words[j]):
                swap(words, i, j)
                swap(date, i, j)

print(date)
print(words)
