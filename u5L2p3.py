filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()

rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    print(sym , c, color)
    
colorDefs = [[0] * 2] * numColors
for i in range(numColors):
    colorline =fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    if(sym=='~'):
        sym=
    for i in range(rows):
        a[i] = fh.readline()
        print(a[i],end='')
        
        
        
        
fh.close()=' '
    
    colorDef
    for i in range(rows):
        a[i] = fh.readline()
        print(a[i],end='')
        
        
        
        
fh.close()s[i][0] = sym
    colorDefs[i][1] = color
    
    a=[0]*rows
    x=[]
    for i in range(rows):
        a[i] = fh.readline()
        print(a[i],end='')
        
        
        
        
fh.close()
