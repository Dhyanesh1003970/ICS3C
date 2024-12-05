'''
Name: Dhyanesh Murugesan
Student number: 1003970
Due date: December 6, 2024
Course: ICS3U0-2



VARIABLE DICTIONARY:

t - turtle variable for simpler code

filname -(str) name of file in the directory of the code

fh - variable to read lines of the fils

colordata - the first line of the file and splits it to rows columns and number of colors

rows -(int) number of rows in the file

cols -(int) number of columns in the file

numColors -(int) number of colors in the file

colordefs - array for symbols in the file

colorDefs2 -array for colors in order relative to the symbol array

colorline -(str) reads the color lines and splits it to 'symbol, c , color'

col - array that stores each row of the file that is read
'''

'''
In cordinates and cordinates2 function:

calls -(int) variable to mimic the end of a row that is being printed

y -(int) y cordinates for turtle

x -(int) x cordinates for turtle

p - array that strips one of the line of the array 'col' (in order)

color - color for turtle dots


'''





import math # math libaray
import turtle # turtle libaray

t=turtle.Turtle() # making it easier
 
 
 
 
#function for cordinates in turtle
def cordinates(rows, cols):
    

    calls = cols/2 # col is split in half so it will line up in the middle
    calls = calls*2 #variable to mimic end cordinate of the end of the row
    math.floor(calls)# rounded to be an whole number
    y = rows/2 # same reason as the variable for 'calls' will make it line up in the middle
    y = y*2 # y starting cordinate
    
    
    for i in range(rows): # loop for number of rows in the file
        x= cols/2 #starting x cordinates for rows 
        math.floor(x)#rounded to be a whole number
        x=x*2 # distance between each point relative to radius of dots
        x=x*-1 # sends turtle to the right side of the turtle portle

        p = col[i].strip()# splits each character of the array
        
        for l in range(len(p)):#loop for columns
            if (x<calls):# will make sure turtle does not go past its ending point
                x += 2 # goes forward x # of times when it is down plotting one of the column
                            
                for j in range(numColors): # will loop through the symbols
                                           # to find one that matchs p[l]
                    if(p[l]==colordefs[j]): # seeing if the character of p[l]
                                            # matches one of colordef[j]
                        color  = (colorDefs2[j])# if so colorDef2[j] becomes color and plots it
                        
                plot(x , y, color) # plotting function                
                                              
        y = y-2 # would make turtle go down y when the for loop for L and J are done
                





#function for cordinates in turtle, but it is flipped 180 degrees
def cordinates2(rows, cols):
    
    calls = cols/2# col is split in half so it will line up in the middle
    calls = calls*-2 #variable to mimic end cordinate of the end of the row
    math.floor(calls)# rounded to be an whole numbe
    y = rows/2 # same reason as the variable for 'calls' will make it line up in the middle
    y = y*-2 # y starting cordinate

    
    
    for i in range(rows):# loop for number of rows in the file
        x= cols/2 #starting x cordinates for rows 
        math.floor(x) # same reason as the variable for 'calls' will make it line up in the middle
        x=x*2# y starting cordinate

        p = col[i].strip()# splits each character of the array
        
        for l in range(len(p)):#loop for columns
            if (x>calls):# will make sure turtle does not go past its ending point
                
                x -= 2 # goes back x # of times when it is down plotting one of the column
                            
                for j in range(numColors):# will loop through the symbols
                                           # to find one that ma# seeing if the character of p[l]
                                            # matches one of colordef[j]tchs p[l]
                    if(p[l]==colordefs[j]):# seeing if the character of p[l]
                                            # matches one of colordef[j]
                        color  = (colorDefs2[j])# if so colorDef2[j] becomes color and plots it
                        
                plot(x , y, color) # plotting function                
                                              
        y = y+2 # would make turtle go up y when the for loop for L and J are done








def plot(x , y, color):# plotting function
    turtle.penup()# turtle pen up so no lines show
    turtle.goto(x, y) # turtle goes to cordinates
    turtle.dot(4 , color)# turtle plots the dot
    t.hideturtle()# turtle is hidden from image
   
   
   
filename = "txt.txt" # filename
fh = open(filename, "r") # opening file

colorData = fh.readline() #labling the first line of reading to a variable
colorData.strip() # splits the line

rows,cols,numColors=colorData.split() # catagorizing the line
rows=int(rows) # Data change (str to int)
cols=int(cols)# Data change(str to int)
numColors=int(numColors) #Data change(str to int)
print(rows, cols, numColors) #print the first line of the file


colordefs = [] #array for symbols
colorDefs2= [] #array for colors


for i in range(numColors):# loop to read all the color lines
    colorLine = fh.readline()#reads as many lines as the number of colors
    colorLine.strip() # splits the characters
    sym, c, colors = colorLine.split() # catagorizing the line
    
    
    
    if sym == '~': # since ~ is space, it is changed to ' '
        sym = " "# symbol changed
    
    colordefs.append(sym) # putting the symbols in an array
    colorDefs2.append(colors)# putting the colors in the array in order as the symbols
   
     


col= [0]*rows # array to take the file contents

for k in range(rows):#loop to make fh read all the lines of the file
    col[k]= fh.readline() # reads the lines of the array and appends it to the array 'col'
    
    
    
turtle.bgcolor('gray40') # background change
turtle.tracer(0,0) # makes turtle faster


cordinates(rows, cols) # function to plot and make turtle move to the right spots

t.hideturtle() # hiding turtle from the image

turtle.update() # updating from turtle tracer so the image can show

fh.close() # file closed, for no other problems

    

