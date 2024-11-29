import math
import turtle

t=turtle.Turtle()





    
    
def cordinates():
    
    calls = cols/2

   
    #calls = calls*3
    math.floor(calls)
    y = rows/2
    row = rows/2

   # y = y*3
    #row = row*3
    row=row*-1
    
    
    
    if(rows>=cols):
        call = rows - cols
        call = call*-1
    
    elif(rows<=cols):
        call = cols - rows
        call = call*-1
    
    print(colordefs)
    print(colorDefs2)

    for i in range(len(col)):
        k=0
        x= cols/2
        x=x*3
        x=x*-1

        p = col[i].strip()
        
        for l in range(len(p)):
            if (x<calls):
                
                x += 3
                
                
                for j in range(numColors):
                    if(p[l]==colordefs[j]):
                        color  = (colorDefs2[j])
                        
                        
                        
               
                plot(x , y, color)
                 
                 
                 
            if(x==calls):
                y = y-3
                






def plot(x , y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(3 , color)
   




    






filename = "smiley_emoji_mod.xpm"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colordefs = []
colorDefs2= []


for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, colors = colorLine.split()
    
    for i in range(len(sym)):
        if sym[i]=='"':
            sym[i] =''
    
    
    for i in range(len(colors)):
        if colors[i]=='"':
            colors[i] =''
    
    
    
    
    if sym == '~':
        sym = " "
    
    colordefs.append(sym)
    colorDefs2.append(colors)
   
     


col= [0]*rows

for k in range(rows):
    col[k]= fh.readline()
    
print(col)
    
    
turtle.bgcolor('gray40')

turtle.tracer(0,0)


cordinates()

turtle.update()

fh.close()

    

