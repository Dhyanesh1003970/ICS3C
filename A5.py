filename = 'data.dat'

fh = open(filename, 'r')


title = fh.readline()




givenname = []
surname = []
cctype = []
ccnum = []
expmo = []
expyr = []





for i in range (201):
    l = fh.readline()
    data=[]
    data.append(l)
    l.strip()
    
    for j in range (len(data)):
        if data[j]==',':
            data[j]=' ' 
    
    print(l)
    
    l.strip()
    g,s,c,cn,m,y = data.split()
    print(g)
    
    





print(data)
fh.close
