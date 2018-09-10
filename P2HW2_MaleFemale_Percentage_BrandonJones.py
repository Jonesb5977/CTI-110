# Male compared to female
# 9/10/18
# CTI-110 P2HW2 - Male Female Percentage
# Brandon Jones

# the total amount of people


girls= float(input('enter number of girls in the class'))

boys= float(input('enter number of boys in the class'))

people=girls+boys
#calculate the percentage

boys=boys/people

girls=girls/people

#Display the percent of boys and girls
print('percent of boys is', format(boys, '%'))
print('percent of girls is', format(girls, '%'))
