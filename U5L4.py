filename = 'words40.dat'

fh= open(filename, 'r')


def swap(B, p, q):
    temp = B[p]
    B[p] = B[q]
    B[q] = temp


ar=[]

for i in range(40):
 
    x = fh.readline()
    x = x.strip()
    ar.append(x)

for i in range(len(ar)):
        for j in range(len(ar)):
            if (ar[i] < ar[j]):
                swap(ar, i, j)
                
print(ar)
