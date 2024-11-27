import math
import turtle

t=turtle.Turtle()





def colors(fh):
    
    c=1
    
    print(colorDefs)
    print(colorDefs2)
    for i in range(rows):
        colorFind = fh.readline()
        colorFind.strip()
        colorFind.split()
        for k in range(cols):
            
            while(colorDefs==colorFind):
                if(colorFind[i]==colorDefs[c]):
                    color = colorDefs2[c]
                    
                
                while(c<=colorDefs):
                    c +=1
    
    cordinates()
    
    
def cordinates(color):
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



    for k in range(rows):
        for l in range(cols):
            while(y>row):
                x= cols/2
                x=x*10
                x=x*-1
                x = x +10
                y = y -10
                plot(x , y)
                while(x<calls):
                    x += 10
                    
                    plot(x , y)



def plot(x , y, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(
    10 , color)
    



    






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
    
    
      
    #if(sym=='~'):
     #   sym=' ' 
            
    
    colorDefs.append([sym])
    colorDefs2.append([color])
     
    
    print(sym, c, color)
    
   
colors(sym,colors, fh)



fh.close()

    

