# A brief description of the project
# 9/26/18
# CTI-110 P4HW3 - Tuition Increase
# Brandon Jones


year=int(input('enter a number 1-5 to find out what the tuition will be'))
t=8000
if year <= 5:
    print(year)
    t2=t*(.03*year)
    print(t2)
else:
    print('Error')
