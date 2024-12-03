import math
import turtle

t=turtle.Turtle()
    
def cordinates(rows, cols):
    
    calls = cols/2
    calls = calls*2
    math.floor(calls)
    y = rows/2
    y = y*2
    
    
    for i in range(rows):
        x= cols/2
        math.floor(x)
        x=x*2
        x=x*-1

        p = col[i].strip()
        
        for l in range(len(p)):
            if (x<calls):
                
                x += 2
                            
                for j in range(numColors):
                    if(p[l]==colordefs[j]):
                        color  = (colorDefs2[j])
                        
                plot(x , y, color)                
                                              
        y = y-2
                






def cordinates2(rows, cols):
    
    calls = cols/2
    calls = calls*-2
    math.floor(calls)
    y = rows/2
    y = y*-2

    
    
    for i in range(rows):
        k=0
        x= cols/2
        math.floor(x)
        x=x*2

        p = col[i].strip()
        
        for l in range(len(p)):
            if (x>calls):
                
                x -= 2
                            
                for j in range(numColors):
                    if(p[l]==colordefs[j]):
                        color  = (colorDefs2[j])
                        
                plot(x , y, color)                
                                              
        y = y+2








def plot(x , y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(4 , color)
    t.hideturtle()
   
   
   
filename = "rocky_bullwinkle_mod.xpm"
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
    
    
    
    if sym == '~':
        sym = " "
    
    colordefs.append(sym)
    colorDefs2.append(colors)
   
     


col= [0]*rows

for k in range(rows):
    col[k]= fh.readline()
    
    
    
turtle.bgcolor('gray40')
turtle.tracer(0,0)


cordinates(rows, cols)

t.hideturtle()

turtle.update()

fh.close()

    

