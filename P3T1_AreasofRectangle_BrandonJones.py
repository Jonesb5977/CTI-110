# CTI-110 
# P3T1 - Length of rectangles 
# Brandon Jones 
# 9/15/18

#get the deminisons of rectangle 1 
length1=int(input('enter the legth of rectangle1...'))
width1=int(input('enter the width of rectangle1...'))

#get the deminsions of rectangle 2
length2=int(input('enter the length of rectangle2...'))
width2=int(input('enter the width of rectangle2...'))

#calculate the areas
area1=width1*length1
area2=width2*length2

#determine which is greater
if area1>area2:
    print('rectangle 1 has the greater area')
elif area2>area1:
    print('rectangle 2 has the greater area')
else:
    print('the area of both rectangles are the same')
