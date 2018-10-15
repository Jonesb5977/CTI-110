# A brief description of the project
# 9/25/18
# CTI-110 P4HW1 - Budget Analysis
# Brandon Jones
#

Budget=float(input('enter ammount budgeted for this month'))

moreexpenses=input('If there is more expenses "T"')
userTotal=0
while moreexpenses =='T':
    Expense=float(input('enter expense'))
    moreexpenses=input('If there is more expenses "T"')
    userTotal += Expense
    evenmoreexpenses=input('enter another expense')

if userTotal>Budget:
   print('You were over your budget by', userTotal-Budget)

elif userTotal<Budget:
   print('You were under your budget by', Budget-userTotal)
