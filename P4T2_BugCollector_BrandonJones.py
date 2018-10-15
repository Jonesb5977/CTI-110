# A brief description of the project
# 9/24/18
# CTI-110 P4T2 - Bug Collector
# Brandon Jones

#iniialize the accumulator
total=0

#get the bugs collected
for day in range(1,8):
    print('enter the bugs collected on day', day)
    bugs=int(input())
    total=total+bugs

#display the number of bugs
    print(' you collected a total of', total, 'bugs')
          
