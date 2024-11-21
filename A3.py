import math
import turtle

t=turtle.Turtle()



def color(s, c):
    if()
    


def cor(x , y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10 , "black")
    



    






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
                   cor(x , y)
                   while(x<calls):
                       x += 10
                       cor(x , y)


                  

fh.close()

filename = "txt.txt"
fh = open(filename, "r")

for i in range(numColors+1):
    fh.readline()

for j in range(rows):
    fh.readline()
    

