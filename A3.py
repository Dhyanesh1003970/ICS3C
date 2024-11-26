import math
import turtle

t=turtle.Turtle()





def colors(sym, color, fh):
    print(colorDefs)
    for i in range(rows):
       colorFind = fh.readline()
       colorFind.strip()
       for j in range(cols):
           for c in range(len(colorDefs)):
               if(colorFind!=colorDefs[c]):
                   print(c)
                

def cordinates():
    x = cols/2
    calls = cols/2

    x = x*10
    calls = calls*10
    y = rows/2
    row = rows/2

    y = y*10
    row = row*10
    row=row*-1
    x = x*-1



    for j in range(rows):
        for i in range(cols):
            while(y>row):
                x= cols/2
                x=x*10
                x=x*-1
                x = x +10
                y = y -10
                plot(x , y, colors)
                while(x<calls):
                    x += 10
                    
                    plot(x , y, colors)



def plot(x , y, colors):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10 , colors)
    



    






filename = "txt.txt"
fh = open(filename, "r")

colorData = fh.readline()
colorData.strip()

rows,cols,numColors=colorData.split()
rows=int(rows)
cols=int(cols)
numColors=int(numColors)
print(rows, cols, numColors)



colorDefs = []
colorDefs2= []


for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, color = colorLine.split()
    
    
      
    if(sym=='~'):
        sym=' ' 
            
    
    colorDefs.append([sym])
    colorDefs2.append([color])
        
    

    print(sym, c, color)
    
   
colors(sym,colors, fh)

    



cordinates()



fh.close()

    

