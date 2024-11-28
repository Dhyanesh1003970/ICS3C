import math
import turtle

t=turtle.Turtle()





#def colors(fh):
    
   
    
 #   print(colorDefs)
  #  print(colorDefs2)
   # for i in range(rows):
    #    colorFind = fh.readline()
     #   colorFind.strip()
      #  colorFind.split()
     
            
       #     while(colorDefs==colorFind):
        #        if(colorFind[i]==colorDefs[c]):
         #           color = colorDefs2[c]
                    
                
          #      while(c<=colorDefs):
           #         c +=1
    
    #cordinates()
    
    
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

    

    for i in range(rows):
        
        x= cols/2
        x=x*10
        x=x*-1

        
        p = col[i].strip()
        
        for l in range(cols):
            if (x<calls):
                
                color = ['black']
                
                
                x += 10
                
                for j in range(numColors):
                    if(p[l]==colordefs[j]):
                        color.append(colorDef2[j])
                
                
                print(color)
               
                plot(x , y, color[0])
    
            if(x==calls):
                y -= 10
                



def plot1(x,y):
    turtle.goto(x, y)




def plot(x , y, colr):
    turtle.penup()
    turtle.goto(x, y)
    turtle.dot(10 , colr)




    






filename = "txt.txt"
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
    
    colordefs.append([sym])
    colorDefs2.append([colors])
   
     


col= [0]*rows

for k in range(rows):
    col[k]= fh.readline()
    
print(col)
    
    
cordinates()



fh.close()

    

