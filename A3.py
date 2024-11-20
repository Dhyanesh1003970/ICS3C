import math
import turtle

t=turtle.Turtle()


def cor(x , y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10 , "black")
    



#def plotIt(x, y, d, color):
 
filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colorDefs = [[0]*2]*numColors
for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    print(sym , c, color)
    
    
    if(sym=='~'):
        sym=' ' 
             
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    
d = 4




x = cols/2
x = x*10


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()
y = rows/2
y = y*10

x = x*-1


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()  






filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colorDefs = [[0]*2]*numColors
for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    print(sym , c, color)
    
    
    if(sym=='~'):
        sym=' ' 
             
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    
d = 4




x = cols/2
x = x*10


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()
y = rows/2
y = y*10

x = x*-1


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()

#def colors():
    



#def plotIt(x, y, d, color):
 
filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colorDefs = [[0]*2]*numColors
for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    print(sym , c, color)
    
    
    if(sym=='~'):
        sym=' ' 
             
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    
d = 4




x = cols/2
x = x*10


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()
y = rows/2
y = y*10

x = x*-1


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()  






filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colorDefs = [[0]*2]*numColors
for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    print(sym , c, color)
    
    
    if(sym=='~'):
        sym=' ' 
             
    colorDefs[i][0] = sym
    colorDefs[i][1] = color
    
d = 4




x = cols/2
x = x*10


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)

fh.close()
y = rows/2
y = y*10

x = x*-1


for j in range(rows):
    
   
    
    for i in range(cols):
        x += 10 
        cor(x , y)


    x= cols/2
    x=x*10
    x=x*-1
    x = x +10
    y = y -10
    cor(x , y)
