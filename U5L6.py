def triangle (ch, num):
    
    if num==1:
        print(ch)
        return
    else:
        print(ch*num)
        num-=1
        triangle(ch, num)
  
    

# DO NOT ALTER CODE AFTER THIS COMMENT
c = "#"
n = 7
triangle(c, n)
