filename= 'wordle.dat'

fh=open(filename, 'r')



def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp








words=[]
for i in range (1038):
    wrd = fh.readline()
    wrd.strip()
    
    mon, dat, yer, word=wrd.split()
    words.append(word)




for i in range(len(words)):
        for j in range(len(words)):
            if (words[i] < words[j]):
                swap(words, i, j)



print(words)
