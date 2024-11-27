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
        c=1
        
        for l in range(cols):
            while(y>row):
              
                
                colorFind = fh.readline()
                colorFind.strip()
        
                #print(colorFind)
                
     
                
                if(colorFind[l]==colorDefs[c]):
                    color = colorDefs2[c]
                    
                    
                else:
                    while(c<=len(colorDefs)):
                        c +=1
                
                
                
                
                
                
                x= cols/2
                x=x*10
                x=x*-1
                x = x +10
                y = y -10
                plot(x , y, color)
                while(x<calls):
                    x += 10
                    
                    plot(x , y, color)



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



colorDefs = []
colorDefs2= []


for i in range(numColors):
    colorLine = fh.readline()
    colorLine.strip()
    sym, c, colors = colorLine.split()
    
    
      
    if(sym=='~'):
        sym=' ' 
            
    
    colorDefs.append(sym)
    colorDefs2.append(colors)
     
    
    print(sym, c, colors)
    
  

cordinates()



fh.close()

    

