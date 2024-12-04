'''
Name: Dhyanesh Murugesan
Student number: 1003970
Due date: December 6, 2024
Course: ICS3U0-2



VARIABLE DICTIONARY:

t




'''





import math
import turtle

t=turtle.Turtle() # making it easier
 
 
 
 
#function for cordinates in turtle
def cordinates(rows, cols):
    

    calls = cols/2
    calls = calls*2 #variable to mimic end cordinate of the end of the row
    math.floor(calls)
    y = rows/2
    y = y*2 # y starting cordinate
    
    
    for i in range(rows):
        x= cols/2 #starting x cordinates for rows 
        math.floor(x)
        x=x*2
        x=x*-1

        p = col[i].strip()# splits each character of the array
        
        for l in range(len(p)):
            if (x<calls):
                x += 2 # goes forward x # of times when it is down plotting one of the column
                            
                for j in range(numColors):
                    if(p[l]==colordefs[j]): # seeing if the character of p[l]
                                            # matches one of colordef[j]
                        color  = (colorDefs2[j])# if so colorDef2[j] becomes color and plots it
                        
                plot(x , y, color) # plotting function                
                                              
        y = y-2 # would make turtle go down y when the for loop for L and J are done
                





#function for cordinates in turtle, but it is flipped 180 degrees
def cordinates2(rows, cols):
    
    calls = cols/2
    calls = calls*-2 #variable to mimic end cordinate of the end of the row
    math.floor(calls)
    y = rows/2
    y = y*-2 # y starting cordinate

    
    
    for i in range(rows):
        x= cols/2 #starting x cordinates for rows 
        math.floor(x)
        x=x*2

        p = col[i].strip()# splits each character of the array
        
        for l in range(len(p)):
            if (x>calls):
                
                x -= 2 # goes back x # of times when it is down plotting one of the column
                            
                for j in range(numColors):
                    if(p[l]==colordefs[j]):
                        color  = (colorDefs2[j])
                        
                plot(x , y, color) # plotting function                
                                              
        y = y+2 # would make turtle go up y when the for loop for L and J are done








def plot(x , y, color):
    turtle.penup()# turtle pen up so no lines show
    turtle.goto(x, y) # turtle goes to cordinates
    turtle.dot(4 , color)# turtle plots the dot
    t.hideturtle()# turtle is hidden from image
   
   
   
filename = "txt.txt"
fh = open(filename, "r") # opening file

colorData = fh.readline() #labling the first line of reading to a variable
colorData.strip() # splits the line

rows,cols,numColors=colorData.split() # catagorizing the line
rows=int(rows) # Data change (str to int)
cols=int(cols)# Data change(str to int)
numColors=int(numColors) #Data change(str to int)
print(rows, cols, numColors)


colordefs = [] #array for symbols
colorDefs2= [] #array for colors


for i in range(numColors):
    colorLine = fh.readline()#reads as many lines as the number of colors
    colorLine.strip() # splits the characters
    sym, c, colors = colorLine.split() # catagorizing the line
    
    
    
    if sym == '~': # since ~ is space, it is changed to ' '
        sym = " "
    
    colordefs.append(sym) # putting the symbols in an array
    colorDefs2.append(colors)# putting the colors in the array in order as the symbols
   
     


col= [0]*rows # array to take the file contents

for k in range(rows):
    col[k]= fh.readline() # reads the lines of the array and appends it to the array 'col'
    
    
    
turtle.bgcolor('gray40') # background change
turtle.tracer(0,0) # makes turtle faster


cordinates(rows, cols) # function to plot and make turtle move to the right spots

t.hideturtle() # hiding turtle from the image

turtle.update() # updating from turtle tracer so the image can show

fh.close() # file closed, for no other problems

    
