# CTI-110 
# P3HW2 - Shipping Charges 
# Brandon Jones
# 9/16/18
#

#Input weight
package=int(input('Input the weight of the package'))

#calculate the shipping charge
if package<=2:
   print('it is $1.5 per pound')
elif 2< package <6:
   print('it is $3 per pound')
elif 6< package <10:
   print('it is $4 per pound')
elif package>10:
   print('it is $4.75 per pound')

